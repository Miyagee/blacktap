<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">

    <style>
      html, body {
      	font-family: 'Arial';
        height: 100%;
        margin: 0;
        padding: 0;
      }
      #map {
      	height: 90%;
      }
    </style>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>

    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAh-RQ7cnK98QkQdYvVseC4Gn34UsPY-Hk&callback=init"
	async defer></script>
</head>
<body>
	<div class="col-md-12 col-sm-12 col-xs-12"><h1>Map:</h1></div>
	<div class="col-md-12 col-sm-12 col-xs-12" id="map"></div>
	<!-- Include php file -->
	<?php include 'php/map_data.php';?>

</body>

	<!-- Parses and loads cords into google api map -->
	<script type="text/javascript">
	function init() {
	  var cord_data = <?php Print(json_encode($map_data)); ?>;
	  var data = [];

			for(var i = 0; i < cord_data.length; i++) {

			    var lat = cord_data[i].lat;
			    var lng = cord_data[i].lng;
			    var weight = cord_data[i].fuel_usage10;

			    if (lng != 0 && lat != 0) {
			    data.push({
			      "lng" : parseFloat(lng),
				  "lat" : parseFloat(lat),
				  "weight" : parseFloat(weight)

			    });
			  }
			}

	  initMap(JSON.stringify(data), data[0]);
	}

	/**
	   * The CenterControl adds a control to the map that recenters the map on
	   * Chicago.
	   * This constructor takes the control DIV as an argument.
	   * @constructor
	   */
	  function CenterControl(controlDiv, map, startPos) {

	    // Set CSS for the control border.
	    var controlUI = document.createElement('div');
	    controlUI.style.backgroundColor = '#fff';
	    controlUI.style.border = '2px solid #fff';
	    controlUI.style.borderRadius = '3px';
	    controlUI.style.boxShadow = '0 2px 6px rgba(0,0,0,.3)';
	    controlUI.style.cursor = 'pointer';
	    controlUI.style.marginBottom = '22px';
	    controlUI.style.textAlign = 'center';
	    controlUI.title = 'Click to recenter the map';
	    controlDiv.appendChild(controlUI);

	    // Set CSS for the control interior.
	    var controlText = document.createElement('div');
	    controlText.style.color = 'rgb(25,25,25)';
	    controlText.style.fontFamily = 'Roboto,Arial,sans-serif';
	    controlText.style.fontSize = '16px';
	    controlText.style.lineHeight = '38px';
	    controlText.style.paddingLeft = '5px';
	    controlText.style.paddingRight = '5px';
	    controlText.innerHTML = 'Center Map';
	    controlUI.appendChild(controlText);

	    // Setup the click event listeners: simply set the map to Chicago.
	    controlUI.addEventListener('click', function() {
	      map.setCenter(startPos);
	    });

	  }

	function initMap(cord_data, startPos) {
			var latlong = {'lat': 58.1479823, 'lng': 7.920251800000001};
			var map = new google.maps.Map(document.getElementById('map'), {
				center: startPos,
				zoom: 14,
				});
				var jsonData = JSON.parse(cord_data);
				var path = new google.maps.Polyline({
				path: jsonData,
				geodesic: true,
				strokeColor: '#FF0000',
				strokeOpacity: 1.0,
				strokeWeight: 2
			});
			path.setMap(map);
			 // Create the DIV to hold the control and call the CenterControl()
	        // constructor passing in this DIV.
	        var centerControlDiv = document.createElement('div');
	        var centerControl = new CenterControl(centerControlDiv, map, startPos);

	        centerControlDiv.index = 1;
	        map.controls[google.maps.ControlPosition.TOP_CENTER].push(centerControlDiv);
	}
	</script>

	<!-- Resize map size dynamically -->
	<script type="text/javascript">
	resizeMap();
	
	window.onresize = function(event) {
		resizeMap();
	};
	function resizeMap() {
		var windowHeight = "height: " + String(window.innerHeight * 0.8) + "px;";
		document.getElementById('map').setAttribute("style", windowHeight);
	}
	</script>

	<!-- Registers data from buttons -->
	<script type="text/javascript">
	$(function() {
	    console.log( "ready!");
		  $(function(){
		    $('.buttons').click(function(){
		            var myValue = $(this).html();
		            console.log($(this).attr('id'));
		        });
		      });
		 });
	</script>
    
</html>