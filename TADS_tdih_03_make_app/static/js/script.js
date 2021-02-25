// var mymap = L.map('dash_map').setView([0,0], 2);
const lat = 42.88
const long = -78.87
let mymap = L.map('map').setView([lat, long], 2);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    // x: 512,
    // y: 512,
    accessToken: 'pk.eyJ1IjoiYmFndWdsaWEiLCJhIjoiY2tqNHowcmxxMTVndDJ6bnB5eWQza3R4biJ9.ywvTTPhOEHoD1H-FUPjngw'
}).addTo(mymap);