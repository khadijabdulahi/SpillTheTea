const getDestination = document.getElementById('address1')
$.get('/mapbox', response => {
  let token = String(response)

  mapboxgl.accessToken = token
  navigator.geolocation.getCurrentPosition(successLocation, errorLocation, {
    enableHighAccuracy: true
  })
  
  const startLocation = []
  function successLocation(position) {
    setupMap([position.coords.longitude, position.coords.latitude])
    startLocation.push(position.coords.longitude, position.coords.latitude)
  }
  
  function errorLocation() {
    setupMap([-2.24, 53.48])
  }

  function setupMap(center) {
    const map = new mapboxgl.Map({
      container: "map",
      style: "mapbox://styles/mapbox/streets-v11",
      center: center,
      zoom: 15
    })
  
    // const nav = new mapboxgl.NavigationControl()
    // map.addControl(nav)
  
    // let directions = new MapboxDirections({
    //   accessToken: mapboxgl.accessToken
    // })
      
    // map.addControl(directions, "top-left")

    map.on('load', function() {
      var directions = new MapboxDirections({
      accessToken: mapboxgl.accessToken
      });
      map.addControl(directions, 'top-left');

      directions.setOrigin('Minneapolis, MN');
      directions.setDestination(getDestination.innerText);
  });
  }

})


$(".test").click(function(){
  $("#exampleModal").modal("show");
});

$("#closebutton").click(function(){
  $("#exampleModal").modal("hide");
})
