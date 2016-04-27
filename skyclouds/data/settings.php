<html>
   
   <head>
      <title>Update a Record in MySQL Database</title>
   </head>

   <style>
      html, body {
         font-family: 'Arial';
      }
   </style>
   
   <body>
      <?php
         if(isset($_POST['update'])) {
            $dbhost = 'mysql.stud.ntnu.no';
            $dbuser = 'skyclouds_admin';
            $dbpass = 'blacktap';
            
            $conn = mysql_connect($dbhost, $dbuser, $dbpass);
            
            if(! $conn ) {
               die('Could not connect: ' . mysql_error());
            }

            $settingsValues = array("speed", "reckless", "odometer", "fuelLast", "fuel", "maxLast", "avgLast", "mapLast", "distanceLast");
      
            $myquery = (
                  "UPDATE skyclouds_blacktap.settings SET "
            );
            
            $i = 0;
            foreach($settingsValues as $pre_value) {
               if(in_array($pre_value, $_POST)) {
                  $myquery = $myquery . ($pre_value . "= 1, ");
                  $_SESSION['settings'][$i] = 1;
               } else {
                  $myquery = $myquery . ($pre_value . "= 0, ");
                  $_SESSION['settings'][$i] = 0;
               }
               $i++;
            }
      
            $myquery = substr($myquery, 0 ,-2);
            
            $myquery = ($myquery . " WHERE brukernavn = '" . $_SESSION['login_user'] . "'");

            mysql_select_db('skyclouds_blacktap');
            $retval = mysql_query( $myquery, $conn );
            
            if(! $retval ) {
               die('Could not update data: ' . mysql_error());
            }
            echo "Updated data successfully\n";
            
            mysql_close($conn);
         }else {
            ?>
               <h1>Settings</h1>
               <form method = "post" action = "<?php $_PHP_SELF ?>">
                  <?php
                     include 'getSettings.php';
                  ?>
                  <input name = "update" type = "submit" id = "update" value = "Update">
               </form>
            <?php
         }
      ?>
      
   </body>
</html>