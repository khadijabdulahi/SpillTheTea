// Once the page is loaded 
$(window).on("load", function () {

  // grabs 3 different class in the button in the all tea's page 
  // each increments through all the favorite tea buttons 
  $('.btn.btn-primary.fav-button').each(function(i, obj) {
    //test

    $.get('/check_favorites/' + obj.id, response => {
      console.log(typeof response)
      if(response == 'true'){
        $(this).addClass('btn btn-danger fav-button')
      }else{
        $(this).addClass('btn btn-primary fav-button')
      }
    })

  });
});        

$("button.fav-button").click(function() {
  // alert(this.id); // or alert($(this).attr('id'));
  // alert($(this).attr('class'))

  if ($(this).attr('class') == "btn btn-primary fav-button") {
    // event.preventDefault()
    // alert($(this).attr('class'))
    $.post('/favorite_action/'+ this.id, response => {
      console.log(response)
        if(response == "Added tea"){
          $(this).removeClass('btn btn-primary fav-button')
          $(this).addClass('btn btn-danger fav-button')
        }
      });
  } else {
      // event.preventDefault()
    $.post('/favorite_action/' + this.id, response => {
      console.log(response)
        if(response == "Removed tea"){
        $(this).removeClass('btn btn-danger fav-button')
        $(this).addClass('btn btn-primary fav-button')
      }
  });
  }
});