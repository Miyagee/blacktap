<?php
        
    $username = "skyclouds_admin"; 
    $password = "blacktap";   
    $host = "mysql.stud.ntnu.no";
    $database="skyclouds_blacktap";
    
    $server = mysql_connect($host, $username, $password);
    $connection = mysql_select_db($database, $server);

    $myquery = "Select longitude as lng, latitude as lat from skyclouds_blacktap.data";
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