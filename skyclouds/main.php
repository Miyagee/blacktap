<?php
	include 'php/login_test.php';
?>
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>BlackTap</title>

    <!-- Custom CSS -->
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
    <link href="css/simple-sidebar.css" rel="stylesheet">
    <style type="text/css">
        @font-face { font-family: skyclouds-body; src: url('fonts/MyriadPro-Light.otf');}

        html,body {
            height: 100%;
            font-family: skyclouds-body;
        }
        .navbutton {
            position: fixed;
            margin-top: -10px;
            background-color:white;
        }
    </style>
</head>
<body>
    <div id="wrapper">
        <!-- Sidebar -->
        <div id="sidebar-wrapper">
            <ul class="sidebar-nav">
            <?php include 'php/load_sidebar.php' ?>
              <li>
                <br>
              </li>
              <li id="php/logout"><a href="php/logout.php">Log out</a></li>
            </ul>
        </div>
        <!-- /#sidebar-wrapper -->

        <!-- Page Content -->
        <div id="page-content-wrapper">
            <div class="container-fluid">
                <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" style="margin-left: -50px;">
                        <button type="button" href="#menu-toggle" class="btn btn-default navbutton" id="menu-toggle">
                            <span class="glyphicon glyphicon-th-list"></span>
                            Menu
                        </button>
                    </div>
                    <div>
                        <?php include 'php/load.php' ?>
                    </div>
                </div>
            </div>
        </div>
        <!-- /#page-content-wrapper -->

    </div>
    <!-- /#wrapper -->

    <!-- jQuery -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>

    <!-- Menu Toggle Script -->
    <script>
    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });
    </script>

</body>

<script type="text/javascript" src="js/activateNavBar.js"></script>

</html>
