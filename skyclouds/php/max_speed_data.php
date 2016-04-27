<?php

    session_start();
    require_once 'php/conn.php';
    
    $server = mysql_connect($hn, $un, $pw);
    $connection = mysql_select_db($db, $server);

    $tripID = $_SESSION['selected_trip'];
    $myquery = "SELECT ROUND(MAX(vehicle_speed), 2) AS 'Max speed' FROM skyclouds_blacktap.data WHERE tripID = $tripID";
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