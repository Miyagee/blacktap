<?php
    
    session_start();

    require_once 'php/conn.php';
    
    $server = mysql_connect($hn, $un, $pw);
    $connection = mysql_select_db($db, $server);

    $tripID = $_GET['tripId'];
    $column = $_GET['column'];

    $myquery = "Select longitude as lng, latitude as lat, $column as col from skyclouds_blacktap.data where tripId='$tripID'";
    $query = mysql_query($myquery);
    
    if ( ! $query ) {
        echo mysql_error();
        die;
    }
    
    $map_data = array();
    
    for ($x = 0; $x < mysql_num_rows($query); $x++) {
        $map_data[] = mysql_fetch_assoc($query);
    }
     
    mysql_close($server);

    echo json_encode($map_data);
?>

