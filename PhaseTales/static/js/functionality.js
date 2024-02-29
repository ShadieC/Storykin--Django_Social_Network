 const user_details = document.querySelector(".user-details");
 const username_icon = document.querySelector(".username-icon");
 const submenu = document.querySelector(".nav-list-submenu");

    if($(".username-icon").length){
      username_icon.addEventListener('click', function(e) {   
        if (user_details.classList.contains("open")) {
           user_details.classList.remove('open');
        } else {
           clear(); 
           user_details.classList.add('open') 
        }   
      })
    }

 const notify = document.querySelector(".notify");
 const notify_icon = document.querySelector(".notify_icon");

    if($(".notify_icon").length){
      notify_icon.addEventListener('click', function(e) {      
        if (notify.classList.contains("open")) {
            notify.classList.remove('open');
        } else {
            clear();
           notify.classList.add('open');
        }
        
      })
    }

const opt_btns = document.querySelectorAll(".more");
const menu = document.querySelector("#option");



// functions
function getOffset(el) {
    const rect = el.getBoundingClientRect();
    return {
        left: rect.left + window.scrollX,
        top: rect.top + window.scrollY + rect.height,
    };
}
function toggle_option(button)
{
    if (menu.style.visibility == "visible")
    { 
        button.classList.remove("current-more");
        menu.style.visibility = "hidden";
        menu.style.top =  "0px";
        menu.style.left = "0px";
    }
    else
    {
        button.classList.add("current-more");
        menu.style.visibility = "visible";
        menu.style.top =  getOffset(button).top + "px";
        menu.style.left = getOffset(button).left - 305 + "px";
    }
}

function toggle_option_update(button)
{
        menu.style.top =  getOffset(button).top + "px";
        menu.style.left = getOffset(button).left - 305 + "px";
}


$(".phase_container").scroll(function(){
    document.querySelectorAll('.more').forEach(function(button) {
        if ( button.classList.contains('current-more') ) {
              toggle_option_update(button);
        }
    });
});

$(".main-blogs").scroll(function(){
  document.querySelectorAll('.more').forEach(function(button) {
        if ( button.classList.contains('current-more') ) {
            toggle_option_update(button);
        }
    });
});

$(".stream-area").scroll(function(){
  document.querySelectorAll('.more').forEach(function(button) {
        if ( button.classList.contains('current-more') ) {
            toggle_option_update(button);
        }
    });
});

$(".main-container").scroll(function(){
    document.querySelectorAll('.more').forEach(function(button) {
        if ( button.classList.contains('current-more') ) {
            toggle_option_update(button);
        }
    });
});

document.querySelectorAll('.profile-menu-link').forEach(function(button) {
    button.addEventListener('click', function() {
        if ( button.classList.contains('active-profile') ) {

        } else {
            $(".active-profile").removeClass("active-profile");
            $(button).addClass("active-profile");
            const content_id = button.getAttribute("for");
            const content = document.getElementById(content_id);
            $(".selected-profile-box").removeClass("selected-profile-box");
            $(content).addClass("selected-profile-box");
        }
    });
});


function myFunction() {
  var dots = document.getElementById("dots");
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("myBtn");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more";
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less";
    moreText.style.display = "inline";
  }
}



function modal_toggle_option(button)
{
    const container = button.closest('.modal-scrollable-container');
    const modalOption = container.querySelector(".modal_option");
    if (modalOption.style.display === 'block'){ 
        button.classList.remove("current-more");
        modalOption.style.display = 'none';
        modalOption.style.top =  "0px";
        modalOption.style.left = "0px";
    }
    else
    {
        button.classList.add("current-more");
        // Calculate the position of the button
        const buttonRect = button.getBoundingClientRect();
        const containerRect = container.getBoundingClientRect();

        // Create and style the modal option
        //const modalOption = document.createElement('div');
        //modalOption.className = 'modal_option';
        //container.appendChild(modalOption);

        // Position the modal option below the button

        const position = container.scrollTop;
        if (position < 0.5 ) {
            modalOption.style.top = `${buttonRect.top - containerRect.top + buttonRect.height }px`;
            modalOption.style.left = `${buttonRect.left - containerRect.left - 305}px`;
        } else  {
            modalOption.style.top = `${buttonRect.top - containerRect.top + container.scrollTop + buttonRect.height}px`;
            modalOption.style.left = `${buttonRect.left - containerRect.left - 305}px`;
        }

        // Show the modal option
        modalOption.style.display = 'block';
    }
}


window.addEventListener('resize', function() {
    if($(".modal_option").length){
        // Check if the modal option is displayed
        if($(".current-more").length){
            const button = document.querySelector('.current-more');
            const container = button.closest('.modal-scrollable-container');
            const modalOption = container.querySelector(".modal_option");
            const isDisplayed = modalOption.style.display === 'block';
          
            if (isDisplayed) {
                // Calculate the position of the button
            
                const containerRect = container.getBoundingClientRect();
                const buttonRect = button.getBoundingClientRect();

                // Position the modal option below the button
                const position = container.scrollTop;
                if (position < 0.5 ) {
                    modalOption.style.top = `${buttonRect.top - containerRect.top + buttonRect.height }px`;
                    modalOption.style.left = `${buttonRect.left - containerRect.left - 305}px`;
                } else  {
                    modalOption.style.top = `${buttonRect.top - containerRect.top + container.scrollTop + buttonRect.height}px`;
                    modalOption.style.left = `${buttonRect.left - containerRect.left - 305}px`;
                }
            } 
        }
    }

    const isVisible = menu.style.visibility === 'visible';
    if (isVisible) {
        document.querySelectorAll('.more').forEach(function(button) {
            if ( button.classList.contains('current-more') ) {
                toggle_option_update(button);
            }
        });
    }
});


