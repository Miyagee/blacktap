<?php

    require_once 'php/conn.php';
    $conn = new mysqli($hn, $un, $pw, $db);
    if ($conn->connect_error) die($conn->connect_error);
    
    $query = "SELECT tank FROM skyclouds_blacktap.bil";
        $result = $conn->query($query);
        if (!result) die("Database access failed: " . $conn->error);

        $rows = $result->num_rows;

        $result->data_seek();
        $tank_row = $result->fetch_array(MYSQLI_NUM);
        echo $tank_row[0];

    $result->close();
    $conn->close();
?>