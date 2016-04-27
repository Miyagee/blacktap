<!DOCTYPE html>
<html>
<head>
	<title></title>
	<!-- Load c3.css -->
    <link href="c3/c3.css" rel="stylesheet" type="text/css">

    <!-- Load d3.js and c3.js -->
    <script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>
    <script src="c3/c3.min.js"></script>
    <link href="sidebar/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
	<!-- Fuel left in tank chart and text -->
    <div class="col-lg-6 col-md-6">
        <h1>Max speed:</h1>
        <div id="chart1"></div>
    </div>

	<!-- Fuel left in tank chart and text -->
    <div class="col-lg-6 col-md-6">
        <h1>Average speed:</h1>
        <div id="chart2"></div>
    </div>

    <!-- Graph of usage last trip -->
    <div class="col-lg-12 col-md-12 col-sm-12">
        <h1>Graph of speed from last trip:</h1>
        <div id="chart_usage"></div>
    </div>

    <!-- Chart fuel usage -->
    <script charset="utf-8">

    var chart_usage = c3.generate({
        bindto: '#chart_usage',
        data: {
            json: <?php include 'php/speed_data.php' ?>,
          keys: {
          	value:['vehicle_speed']
          }
        }
    });
    var chart1 = c3.generate({
    	bindto: '#chart1',
        data: {
            json: <?php include 'php/max_speed_data.php' ?>,
            keys:{
            	value:['vehicle_speed']
            },
            type: 'gauge',
            onclick: function (d, i) { console.log("onclick", d, i); },
            onmouseover: function (d, i) { console.log("onmouseover", d, i); },
            onmouseout: function (d, i) { console.log("onmouseout", d, i); }
        },
        gauge: {
          max: 110,// 100 is default
        },
        color: {
            pattern: ['#FF0000', '#F97600', '#F6C600', '#60B044'], // the three color levels for the percentage values.
            threshold: {
                values: [30, 60, 90, 100]
            }
        },
        size: {
            height: 180
        }
    });
    var chart2 = c3.generate({
    	bindto: '#chart2',
        data: {
            json: <?php include 'php/avg_speed_data.php' ?>,
            keys:{
            	value:['vehicle_speed']
            },
            type: 'gauge',
            onclick: function (d, i) { console.log("onclick", d, i); },
            onmouseover: function (d, i) { console.log("onmouseover", d, i); },
            onmouseout: function (d, i) { console.log("onmouseout", d, i); }
        },
        gauge: {
          max: 110,// 100 is default
        },
        color: {
            pattern: ['#FF0000', '#F97600', '#F6C600', '#60B044'], // the three color levels for the percentage values.
            threshold: {
                values: [30, 60, 90, 100]
            }
        },
        size: {
            height: 180
        }
    });
    </script>
</html>