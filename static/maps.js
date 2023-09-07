"use strict";

function initMap() {
  const myLatLng = {
    lat: 53.349266052246094,
    lng: -6.260063171386719
  };
  const map = new google.maps.Map(document.getElementById("gmp-map"), {
    zoom: 11,
    center: myLatLng,
    fullscreenControl: false,
    zoomControl: true,
    streetViewControl: false
  });
  new google.maps.Marker({
    position: myLatLng,
    map,
    title: "My location"
  });
}