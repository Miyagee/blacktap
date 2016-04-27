<?php Session_Start(); ?>
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
        <h1>Last trip's distance:</h1>
        <h2>
            <?php include 'php/lastTrip_distance_data.php' ?> km
        </h2>
    </div>
    </body>
    </html>