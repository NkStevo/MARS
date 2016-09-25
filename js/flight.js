/**
* Created with marsproj.
* User: alissaom
* Date: 2016-09-24
* Time: 04:06 PM
* To change this template use Tools | Templates.
*/
 
var flightNum; 
var user;
var flight_status_url = "https://demo30-test.apigee.net/v1/hack/status"
var airport_search_url = "https://demo30-test.apigee.net/v1/hack/search/airport"
var flight_schedule_url = "https://demo30-test.apigee.net/v1/hack/schedule"
var flight_search_url = "https://demo30-test.apigee.net/v1/hack/search/flight"
var distance_matrix_url = "https://maps.googleapis.com/maps/api/distancematrix/json"


var distance_matrix_api_key = "AIzaSyCqcO7IsQMdP15hsUBBRzzaB-Gs6sc3e5I"

function loadFlight(flightNumber,firstName) {
    
    //define variables
  
//     var flightStuff = JSON.parse(flightNum.responseText);
     user = firstName;
     flightNum = flightNumber;
    
        alert("Hi there");

    //pull HTML elements
//     document.getElementById('origin').innerHTML = flightStuff.origin;
//     document.getElementById('destination').innerHTML = flightStuff.destination;
//     document.getElementById('').innerHTML = flightStuff.;
    
}


function flightNumber(){
    return flightNum;
}

document.getElementById('userMsg').innerHTML = flightNumber();


function flight_search() {
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //January is 0!
    var yyyy = today.getFullYear();

    if(dd<10) {
        dd='0'+dd
    } 

    if(mm<10) {
        mm='0'+mm
    } 
    today = yyyy+'-'+mm+'-'+dd;
    
    alert(today);
    $.getJSON(
        flight_status_url,
        {'flightNumber': flightNum, 'flightOriginDate':today, 'apikey': 'N8asxYvgleOXWqX5QcUsn19bmR7ysTN7'},
        function(data) {
            var lat = data['flightStatusResponse']["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["departureAirportCode"];
//             var long = data['longitude_deg'];
           alert('page contents: ' + lat);
            
            
            document.getElementById('userMsg').innerHTML = lat;
        }
    );

}


var getDistance(srcLatLong, dstLatLong) {
    
    getJSON(
        distance_matrix_url,
        {'origins': srcLatLong, 'destinations':dstLatLong, 'apikey': distance_matrix_api_key},
        function(data) {
            var lat = data['flightStatusResponse']["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["departureAirportCode"];
//             var long = data['longitude_deg'];
           alert('page contents: ' + lat);
            
            
            document.getElementById('userMsg').innerHTML = lat;
        }
    );
}


