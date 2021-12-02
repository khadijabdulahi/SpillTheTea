$(window).on("load", function () {
  $('.btn.btn-outline-dark.fav-button').each(function(i, obj) {
    $.get('/check_favorites/' + obj.id, response => {
      console.log(typeof response)
      if(response == 'true'){
        $(this).addClass('btn btn btn-warning fav-button')
      }else{
        $(this).addClass('btn btn-outline-dark fav-button')
      }
    })
  });
});        

$("button.fav-button").click(function() {
  if ($(this).attr('class') == "btn btn-outline-dark fav-button") {
    $.post('/favorite_action/'+ this.id, response => {
      console.log(response)
        if(response == "Added tea"){
          $(this).removeClass('btn btn-outline-dark fav-button')
          $(this).addClass('btn btn btn-warning fav-button')
        }
      });
  } else {
    $.post('/favorite_action/' + this.id, response => {
      console.log(response)
        if(response == "Removed tea"){
        $(this).removeClass('btn btn btn-warning fav-button')
        $(this).addClass('btn btn-outline-dark fav-button')
      }
  });
  }
});