<?php Session_Start(); ?>
<!DOCTYPE html>
<html>
<head>
	<!-- Load c3.css -->
    <link href="c3/c3.css" rel="stylesheet" type="text/css">

    <!-- Load d3.js and c3.js -->
    <script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>
    <script src="c3/c3.min.js"></script>
    <link href="sidebar/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <!-- Print/echo odometer -->
    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
        <h1 style="font-size: 60px;"><span>Welcome </span><span>
        <?php 
            session_start();
            echo ucfirst($_SESSION['login_user']);
        ?></span>
    </div>

    <?php include 'load_dashboard.php' ?>
</body>
</html>