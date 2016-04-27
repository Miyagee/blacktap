<?php

    require_once 'php/conn.php';
    $conn = new mysqli($hn, $un, $pw, $db);
    if ($conn->connect_error) die($conn->connect_error);
    
    $query = "SELECT odometer FROM skyclouds_blacktap.data ORDER BY timestamp DESC LIMIT 1";
        $result = $conn->query($query);
        if (!result) die("Database access failed: " . $conn->error);

        $rows = $result->num_rows;

        $result->data_seek();
        $first_distance = $result->fetch_array(MYSQLI_NUM);

    $query = "SELECT odometer FROM skyclouds_blacktap.data ORDER BY timestamp ASC LIMIT 1";
        $result = $conn->query($query);
        if (!result) die("Database access failed: " . $conn->error);

        $rows = $result->num_rows;

        $result->data_seek();
        $last_distance = $result->fetch_array(MYSQLI_NUM);

       
    $distance = (($first_distance[0] - $last_distance[0]) * 100);

    $query = "SELECT fuel_consumed_since_restart FROM skyclouds_blacktap.data ORDER BY timestamp DESC LIMIT 1";
        $result = $conn->query($query);
        if (!result) die("Database access failed: " . $conn->error);

        $rows = $result->num_rows;

        $result->data_seek();
        $first_fuel = $result->fetch_array(MYSQLI_NUM);

    $query = "SELECT fuel_consumed_since_restart FROM skyclouds_blacktap.data ORDER BY timestamp ASC LIMIT 1";
        $result = $conn->query($query);
        if (!result) die("Database access failed: " . $conn->error);

        $rows = $result->num_rows;

        $result->data_seek();
        $last_fuel = $result->fetch_array(MYSQLI_NUM);

    $total_fuel_consumed = ($first_fuel[0] - $last_fuel[0]);
    
    echo ($total_fuel_consumed / $distance);

    $result->close();
    $conn->close();
?>