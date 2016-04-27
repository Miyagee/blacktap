<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Heatmaps</title>
    <style>
      @font-face { font-family: skyclouds-body; src: url('../fonts/MyriadPro-Light.otf');}
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
        font-family: 'Arial';
        font-size: 14px;
      }
      #map {
        height: 100%;
      }
      #floating-panel {
        position: absolute;
        top: 10px;
        left: 25%;
        z-index: 5;
        background-color: #fff;
        padding: 5px;
        border: 1px solid #999;
        text-align: center;
        font-family: 'Roboto','sans-serif';
        line-height: 30px;
        padding-left: 10px;
      }
      #floating-panel {
        background-color: #fff;
        border: 1px solid #999;
        left: 25%;
        padding: 5px;
        position: absolute;
        top: 10px;
        z-index: 5;
      }
    </style>
      <link href="css/simple-sidebar.css" rel="stylesheet">

    <script   src="http://code.jquery.com/jquery-2.2.3.min.js"   integrity="sha256-a23g1Nt4dtEYOj7bR+vTu7+T8VP13humZFBJNIYoEJo="   crossorigin="anonymous"></script>
    <script async defer
        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAh-RQ7cnK98QkQdYvVseC4Gn34UsPY-Hk&libraries=visualization&callback=initMap">
    </script>
  </head>

  <body>
    <div id="sidebar-wrapper">
          <ul class="sidebar-nav">
          <?php include 'php/load_sidebar.php' ?>
            <li>
              <br>
            </li>
            <li id="php/logout"><a href="php/logout.php">Log out</a></li>
          </ul>
      </div>

    <div id="floating-panel">
      <button onclick="toggleHeatmap()">Toggle Heatmap</button>
      <button onclick="changeGradient()">Change gradient</button>
      <button onclick="changeRadius()">Change radius</button>
      <button onclick="changeOpacity()">Change opacity</button>
      Data:
      <select id="column_select">
        <option value="engine_speed">Engine speed</option>
        <option value="vehicle_speed">Vehicle speed</option>
        <option value="fuel_usage10">Fuel user per 10 km</option>
        <option value="steering_wheel_angle">Steering Wheel Angle</option>
        <option value="speeding">Breaking the Speed Limit</option>
        <option value="forgot_signals">Forgot Signals</option>
        <option value="gear_suggestion">Gear Suggestion</option>
        <option value="gear_lever_position">Gear Lever Position</option>
        <option value="torque_at_transmission">Torque At Transmission</option>
        <option value="aggressive">Aggressive Driving</option>
        <option value="brake_pedal_status">Brake Pedal Status</option>
      </select>
      <!--
      tripId:
      <select id="tripId">
      </select>
      -->
    </div>
    <div id="map"></div>
    <script>

      // This example requires the Visualization library. Include the libraries=visualization
      // parameter when you first load the API. For example:
      // <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=visualization">

      var map, heatmap
      var tripId = 21;
      var column = 'engine_speed';
      console.log('LOAD');
      for (var i = 1; i < 25; i++) {
        $('#tripId').append($("<option></option>").attr("value",i).text(i));
      }

      $("#tripId").change(function(event) {
        tripId = parseInt(this.value);
        initMap();
      });

      $("#column_select").change(function(event) {
        column = this.value;
        initMap();
      });

      function initMap() {
        $.get("./map_data.php?column="+column+"&tripId="+tripId).success(function(data) {
          console.log(tripId);
          console.log(column);
          data = JSON.parse(data);

          points = []
          maxIntensity = 0
          for (i = 0; i < data.length; i++) {
            weight = parseInt(data[i].col);
            if (weight > 0) {
              points.push({location: new google.maps.LatLng(data[i].lat, data[i].lng), weight: weight});
              if (weight*4 > maxIntensity) {
                maxIntensity = weight*4;
              }
            }
          }
          map = new google.maps.Map(document.getElementById('map'), {
            zoom: 14,
            center: {lat: parseFloat(data[0].lat), lng: parseFloat(data[0].lng)},
            mapTypeId: google.maps.MapTypeId.ROADMAP
          });
          //console.log(parseFloat(data[0].lat));
          //console.log(parseFloat(data[0].lng));

          heatmap = new google.maps.visualization.HeatmapLayer({
            data: points,
            maxIntensity: maxIntensity,
            dissipating: true,
            map: map
          });
        });
      }

      function toggleHeatmap() {
        heatmap.setMap(heatmap.getMap() ? null : map);
      }

      function changeGradient() {
        var gradient = [
          'rgba(0, 255, 255, 0)',
          'rgba(0, 255, 255, 1)',
          'rgba(0, 191, 255, 1)',
          'rgba(0, 127, 255, 1)',
          'rgba(0, 63, 255, 1)',
          'rgba(0, 0, 255, 1)',
          'rgba(0, 0, 223, 1)',
          'rgba(0, 0, 191, 1)',
          'rgba(0, 0, 159, 1)',
          'rgba(0, 0, 127, 1)',
          'rgba(63, 0, 91, 1)',
          'rgba(127, 0, 63, 1)',
          'rgba(191, 0, 31, 1)',
          'rgba(255, 0, 0, 1)'
        ]
        heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
      }

      function changeRadius() {
        heatmap.set('radius', heatmap.get('radius') ? null : 20);
      }

      function changeOpacity() {
        heatmap.set('opacity', heatmap.get('opacity') ? null : 0.2);
      }

      $(document).ready(function() {
        $("#tripId").val("21");
        $("#column_select").val("engine_speed");
      });

    </script>
  </body>
</html>
