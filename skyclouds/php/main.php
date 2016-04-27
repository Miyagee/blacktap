<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>BlackTap</title>

    <!-- Bootstrap Core CSS -->
    <link href="css/sidebar-bootstrap.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="css/simple-sidebar.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

    <?php include 'php/login_test.php' ?>

</head>

<body>

    <div id="wrapper">

        <!-- Sidebar -->
        <div id="sidebar-wrapper">
            <ul class="sidebar-nav">
                <li class="sidebar-brand">
                    <a href="main.php">
                        BlackTap
                    </a>
                </li>
                <li>
                    <a href="main.php">Dashboard</a>
                </li>
                <li>
                    <a href="main.php?data=car">Bil</a>
                </li>
                <li>
                    <a href="main.php?data=fuel_usage">Bensinforbruk</a>
                </li>
                <li>
                    <a href="main.php?data=gps">GPS</a>
                </li>
                <li>
                    <a href="main.php?data=speed_new">Hastighet</a>
                </li>
                <li>
                  <li>
                      <a href="main.php?data=settings">Instillinger</a>
                  </li>
                </li>
            </ul>
        </div>
        <!-- /#sidebar-wrapper -->

        <!-- Page Content -->
        <div id="page-content-wrapper">
            <div class="container-fluid">
                <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" style="margin-left: -50px;">
                        <button type="button" href="#menu-toggle" class="btn btn-default" id="menu-toggle">
                            <span class="glyphicon glyphicon-th-list"></span>
                            Menu
                        </button>
                    </div>
                    <?php include 'php/load.php' ?>
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

</html>
