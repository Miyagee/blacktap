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
    <div class="col-lg-12 col-md-12 col-sm-12">
        <h1>Graph of fuel usage from last trip:</h1>
        <div id="chart_usage"></div>
    </div>

    <script charset="utf-8">
    var chart_usage = c3.generate({
        bindto: '#chart_usage',
        data: {
          json: <?php include 'php/fuel_usage_data.php' ?>,
          keys: {
          	value:['Fuel used']
          }
        },
        axis: {
            y: {
                label: {
                    text: 'Liter',
                    position: 'outer-middle'
                }
            }
        }
    });
    </script>
</body>
</html>