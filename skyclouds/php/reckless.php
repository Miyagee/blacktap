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
    <div class="col-lg-12 col-md-12">
        <h1>Recklessness</h1>
    </div>
    <div class="col-lg-12 col-md-12">
    	<?php include 'php/reckless_map.php' ?>
    </div>
    </body>
    </html>