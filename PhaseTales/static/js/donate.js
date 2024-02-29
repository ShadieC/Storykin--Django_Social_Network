$(".denomination").click(function(event) {
  $(".denomination").removeClass("selected").prop('checked', false);
  $(".denomination-other input").removeClass("selected").val('');
  $(this).addClass("selected");
  $(this).children(":first").prop('checked', true);
  $("#donate_btn").text('Donate $' + $(this).children(":first").val())
});

$(".denomination-other input").on('keypress', function (event) {
  // allow only int values
  // TODO: remove leading 0
  var regex = new RegExp("^[0-9]+$");
  var key = String.fromCharCode(!event.charCode ? event.which : event.charCode);
  if (!regex.test(key)) {
    event.preventDefault();
    return false;
  }
  
  $(".denomination").removeClass("selected").prop('checked', false);
  $(this).addClass("selected");
  $("#donate_btn").text('Donate $' + $(this).val() + key );
});