var points = [];
var map = null;
$(document).ready(function () {
    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:8000/dustbin/dustbins/?format=json',
        success: function (data) {
            console.log('success', data);
            for (var i = 0; i < data.length; i++) {
                points.push(new google.maps.LatLng(data[i]['latitude'], data[i]['longitude']));
            }
            addMarkers();
        }
    });
});

function addMarkers() {
    var marker, i;
    var size = points.length;
    var default_location = {lat: 0.0, lng: 0.0};
    for (i = 0; i < size; i++) {
        marker = new google.maps.Marker({
            position: points[i],
            map: map,
            title: 'Dustbin',
            icon: 'https://maps.google.com/mapfiles/kml/shapes/parking_lot_maps.png'
        });
        console.log('Success !');
    }
}

function initMap() {
    var default_location = {lat: 0.0, lng: 0.0};
    map = new google.maps.Map(
        document.getElementById('map'), {
            zoom: 4,
            center: default_location,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        });
    addMarkers();
}