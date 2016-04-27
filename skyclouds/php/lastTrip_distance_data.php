<?php

    session_start();

    require_once 'php/conn.php';
    $conn = new mysqli($hn, $un, $pw, $db);
    if ($conn->connect_error) die($conn->connect_error);

    $tripID = $_SESSION['selected_trip']; 

    $query = "SELECT odometer FROM skyclouds_blacktap.data WHERE tripId = $tripID ORDER BY timestamp DESC LIMIT 1";
        $result = $conn->query($query);
        if (!result) die("Database access failed: " . $conn->error);

        $rows = $result->num_rows;

        $result->data_seek();
        $row_first = $result->fetch_array(MYSQLI_NUM);

    $query = "SELECT odometer FROM skyclouds_blacktap.data WHERE tripId = $tripID ORDER BY timestamp ASC LIMIT 1";
        $result = $conn->query($query);
        if (!result) die("Database access failed: " . $conn->error);

        $rows = $result->num_rows;

        $result->data_seek();
        $row_last = $result->fetch_array(MYSQLI_NUM);

       
    echo number_format(($row_first[0] - $row_last[0]), 2, '.', ' ');

    $result->close();
    $conn->close();
?>