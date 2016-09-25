$("#loginForm").submit(function(){
     var name = $("#userName").val();
     var number = $("#flightNum").val();
     var date = $("#date").val();

     var body = {
         "name": name,
         "number": number,
         "date": date
     }

     $.ajax({
          contentType: "application/json",
          url: "/api/flightinfo/" + body.number + "/" + body.date,
          method: "GET",
          data: JSON.stringify(body)
     }).done(function(data) {
          console.log(data);
     }).fail(function(data){ //error messages come in as a diff format than success messages
          console.log("Connection failed!");
     });

     window.location = "http://127.0.0.1:5000/api/flightinfo/" + body.number + "/" + body.date;

    document.getElementById('displayName').innerHTML = "Hi, " + document.getElementById("userName").value + "! ";

     return false;
});
