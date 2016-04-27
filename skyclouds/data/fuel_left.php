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
    <div class="col-lg-6 col-md-6">
        <h1>Fuel left in tank:</h1>
        <div id="chart_left"></div>
    </div>
    <script charset="utf-8">
    var chart = c3.generate({
    	bindto: '#chart_left',
        data: {
            json: <?php include 'php/fuel_level_data.php' ?>,
            keys:{
            	value:['Remaining fuel']
            },
            type: 'gauge',
            onclick: function (d, i) { console.log("onclick", d, i); },
            onmouseover: function (d, i) { console.log("onmouseover", d, i); },
            onmouseout: function (d, i) { console.log("onmouseout", d, i); }
        },
        gauge: {
          max: <?php include 'php/fuel_level_data.php' ?>[0].tank, // 100 is default
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
</body>
</html>