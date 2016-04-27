<?php include 'php/logged_in_test.php' ?>
<!DOCTYPE html>
<html>
<!--
	FILE NAME:	index.html
	WRITTEN BY:	Jie Li & Kevin Midbøe
	WHEN:	February 2016
	PURPOSE:	Login to page
	-->
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name=viewport content="width=device-width, initial-scale=1">
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">

    <link rel="stylesheet" type="text/css" href="css/style.css">
    <link rel="stylesheet" type="text/css" href="css/login.css">
    <title>Black Tap</title>
  </head>
  <body>
    <?php include 'php/login.php'; ?>

      <div class="col-xs-offset-1 col-xs-10 col-sm-offset-3 col-sm-6 col-md-offset-4 col-md-4 centered login-box-container">
        <h1>Black Tap Login</h1>
        <!--Formen tar inn passord og brukernavn og skriver ut feilmelding hvis det ikke stemmer-->
        <form action="" method="post">
          <input id="name"type="text" name="username" placeholder="Brukernavn">
          <input id="password" type="password" name="password" placeholder="Passord">
          <input type="submit" name="submit" class="login login-submit" value=" Login ">
          <span><?php echo $error; ?></span>
        </form>
      </div>

    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
  </body>
</html>
