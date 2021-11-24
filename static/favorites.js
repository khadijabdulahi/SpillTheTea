$(window).on("load", function () {

  $('.btn.btn-primary.fav-button').each(function(i, obj) {
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
  if ($(this).attr('class') == "btn btn-primary fav-button") {
    $.post('/favorite_action/'+ this.id, response => {
      console.log(response)
        if(response == "Added tea"){
          $(this).removeClass('btn btn-primary fav-button')
          $(this).addClass('btn btn-danger fav-button')
        }
      });
  } else {
    $.post('/favorite_action/' + this.id, response => {
      console.log(response)
        if(response == "Removed tea"){
        $(this).removeClass('btn btn-danger fav-button')
        $(this).addClass('btn btn-primary fav-button')
      }
  });
  }
});