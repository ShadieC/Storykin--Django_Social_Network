const phoneInputField = document.querySelector("#phone");
const phoneInputField2 = document.querySelector("#phone2");
    const phoneInput = window.intlTelInput(phoneInputField, {
      utilsScript:
        "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
    });

    const phoneInput2 = window.intlTelInput(phoneInputField2, {
      utilsScript:
        "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
    });

    const info = document.querySelector(".alert-info");
    const field = document.querySelector(".text-value")
    const error = document.querySelector(".alert-error");

    function process(event) {
      event.preventDefault();

      const phoneNumber = phoneInput.getNumber();

      info.style.display = "";
      info.innerHTML = `Phone number in E.164 format: <strong>${phoneNumber}</strong>`;
      field.style.display = "";
      field.value = phoneNumber;
      document.querySelector(".reset-btn").style.display = "inline-block";
      document.querySelector(".reset-btn").addEventListener("click", function(){
        location.reload()
      })
    }