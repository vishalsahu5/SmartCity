
  function initMap(dustbin_points, default_location) {
    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 12,
      center: default_location
    });
    directionsDisplay.setMap(map);

    // add event listener
      calculateAndDisplayRoute(dustbin_points, default_location, directionsService, directionsDisplay);

  }

  function calculateAndDisplayRoute(dustbin_points, default_location, directionsService, directionsDisplay) {
      waypts = [];
      for (var i = 0; i < dustbin_points.length; i++) {
          waypts.push({
            location: dustbin_points[i].latLng,
            stopover: true
          });
      }

    directionsService.route({
      origin: default_location,
      destination: default_location,
      waypoints: waypts,
      optimizeWaypoints: true,
      travelMode: 'DRIVING'
    }, function(response, status) {
      if (status === 'OK') {
        directionsDisplay.setDirections(response);

      } else {
        window.alert('Directions request failed due to ' + status);
      }
    });
  }

  $(document).ready(function () {
      $.ajax({
          type: 'GET',
          url: 'http://127.0.0.1:8000/dustbin/api/dustbins/?format=json',
          success: function (data) {
              var dustbin_points = [];
              var type = "DUSTBIN";
              console.log('success', data);
              for (var i = 0; i < data.length; i++) {
                  if(data[i]['isFull'] === true)
                    dustbin_points.push({'title': data[i]['location'], 'latLng': new google.maps.LatLng(data[i]['latitude'], data[i]['longitude'])});
              }
              var default_location = {lat: 30.3398, lng: 76.3869};
              google.maps.event.addDomListener(window, 'load', initMap(dustbin_points, default_location));
          }
      });

  });
