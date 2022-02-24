function initMap() {
    // The location of nanglerng
    const nanglerng = { lat: 13.7591027, lng: 100.5099457 };
    // The map, centered at nanglerng
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 17,
      center: nanglerng,
    });
    // The marker, positioned at nanglerng
    const marker = new google.maps.Marker({
      position: nanglerng,
      map: map,
    });
  }
  