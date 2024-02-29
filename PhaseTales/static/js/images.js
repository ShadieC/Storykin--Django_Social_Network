function getval(sel) {          
  if (sel.files && sel.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      const preview_container_id = sel.getAttribute("preview");
      const preview_container = document.getElementById(preview_container_id);
      $(preview_container).html("")
      $(preview_container).append('<img class="preview" src="'+e.target.result+'" alt="your image" />');
      
      $(preview_container).append('<button class="btn btn-link deletor" preview="'+preview_container_id+'" onclick="deletor(this);"><small>X</small></button>');
      //$(sel).css('visibility','hidden')
    }

    reader.readAsDataURL(sel.files[0]);
  }    
}

function deletor(btn){
  const preview_container_id = btn.getAttribute("preview");
  const preview_container = document.getElementById(preview_container_id);
  $(preview_container).html("")
}

function getImageEditor(inputId) {
  const sel = document.getElementById(inputId);
  if (sel.files && sel.files[0]) {  
    // Get the selected image file
    const uneditedFile = sel.files[0];

    // Create a new FileReader object
    const reader = new FileReader();

    // Set up the onload event handler
    reader.onload = function(event) {
      const image = new Image();
      image.src = event.target.result;
      image.addEventListener('load', function() {

        const config = {
          cloudimage: {
            token: 'ccnbbxqsda'
          }
        };
        const onComplete = (url, file) => {
          console.log("the file url is: ", url);
          console.log("the main file: ", file);
        }

        const onError = (url, file) => {
          console.error('Error occurred during image editing:', error);
          getval(sel)
        }
        
        const onBeforeComplete = (props) => {
          let imageBase64 = props.canvas.toDataURL();
          const imageBlob = base64ToBlob(imageBase64);
          const imageURL = URL.createObjectURL(imageBlob);

          // Update the input field's value with the edited image file
          sel.src = imageBase64 

          const preview_container_id = sel.getAttribute("preview");
          const preview_container = document.getElementById(preview_container_id);
          $(preview_container).html("")
          $(preview_container).append('<img class="preview" src="'+imageURL+'" onclick="getImageEditor(\''+inputId+'\');" alt="your image" />');
          
          $(preview_container).append('<button class="btn btn-link deletor" preview="'+preview_container_id+'" onclick="deletor(this);"><small>X</small></button>');


        }

        const ImageEditor = new FilerobotImageEditor(config, {
          onComplete: onComplete,
          onBeforeComplete: onBeforeComplete,
          onError: onError,
          onClose: () => {
            ImageEditor.unmount()
          },
        });
        ImageEditor.open(image.src);
        
      });
    };
    reader.readAsDataURL(uneditedFile);
  }
}

const base64ToBlob = (base64) => {
  const bytes = atob(base64.split(',')[1]);
  const mime_type = base64.split(',')[0].split(';')[0].split(':')[1]
  const aB = new ArrayBuffer(bytes.length)
  const u8B = new Uint8Array(aB)
  for (let i = 0; i < bytes.length; i++) {
    u8B[i] = bytes.charCodeAt(i)
  }
  return new Blob([aB], {type: mime_type})
}