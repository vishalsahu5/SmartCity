var map = null;
$(document).ready(function () {
    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:8000/dustbin/api/dustbins/?format=json',
        success: function (data) {
            var dustbin_points = [];
            var type = "DUSTBIN";
            console.log('success', data);
            for (var i = 0; i < data.length; i++) {
                dustbin_points.push(new google.maps.LatLng(data[i]['latitude'], data[i]['longitude']));
            }
            addMarkers(dustbin_points, type);
        }
    });
    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:8000/parking/api/parking_lots/?format=json',
        success: function (data) {
            var parking_points = [];
            var type = "PARKING";
            console.log('success', data);
            for (var i = 0; i < data.length; i++) {
                parking_points.push(new google.maps.LatLng(data[i]['latitude'], data[i]['longitude']));
            }
            addMarkers(parking_points, type);
        }
    });
});

function addMarkers(points, type) {
    var marker, i;
    if (points) {
        var size = points.length;
        if (type === "DUSTBIN") {
            for (i = 0; i < size; i++) {
                marker = new google.maps.Marker({
                    position: points[i],
                    map: map,
                });
                console.log('Success !');
            }
        } else if (type === "PARKING") {
            for (i = 0; i < size; i++) {
                marker = new google.maps.Marker({
                    position: points[i],
                    map: map,
                    icon: 'https://maps.google.com/mapfiles/kml/shapes/parking_lot_maps.png'
                });
                console.log('Success !');
            }
        }

    }
}

function initMap() {
    var default_location = {lat: 30.3398, lng: 76.3869};
    map = new google.maps.Map(
        document.getElementById('map'), {
            center: default_location,
            zoom: 13
            // mapTypeId: google.maps.MapTypeId.ROADMAP
        });
        addMarkers();
}
