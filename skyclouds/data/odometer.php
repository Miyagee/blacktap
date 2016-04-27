<!DOCTYPE HTML>
<html>
<head>
    <title></title>
    <!-- Load c3.css -->
    <link href="c3/c3.css" rel="stylesheet" type="text/css">

    <!-- Load d3.js and c3.js -->
    <script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>
    <script src="c3/c3.min.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
    <link href="sidebar/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="css/odometer.css">
</head>
<body>
    <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
        <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
            <h1>Odometer:</h1>
        </div>
        <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" style="height: 130px;">
            <?php include 'php/odometer_display.php' ?>
        </div>
    </div>
</body>
</html>