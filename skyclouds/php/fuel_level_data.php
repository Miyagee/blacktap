<?php
    Session_Start();
        
    $username = "skyclouds_admin"; 
    $password = "blacktap";   
    $host = "mysql.stud.ntnu.no";
    $database="skyclouds_blacktap";
    
    $server = mysql_connect($host, $username, $password);
    $connection = mysql_select_db($database, $server);

    $tripID = $_SESSION['selected_trip'];

    $myquery = "SELECT fuel_level as 'Remaining fuel', bil.tank FROM skyclouds_blacktap.data INNER JOIN skyclouds_blacktap.bil ON data.bil_idBil = bil.idBil WHERE fuel_level IS NOT null AND tripId = '$tripID' ORDER BY timestamp DESC LIMIT 1";
    $query = mysql_query($myquery);
    
    if ( ! $query ) {
        echo mysql_error();
        die;
    }
    
    $data = array();
    
    for ($x = 0; $x < mysql_num_rows($query); $x++) {
        $data[] = mysql_fetch_assoc($query);
    }
    
    echo json_encode($data);     
     
    mysql_close($server);
?>