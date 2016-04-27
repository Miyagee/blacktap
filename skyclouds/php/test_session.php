<?php
	session_start();
	echo $_SESSION['type'], '<br>';
	echo $_SESSION['login_user'], '<br>';
    echo $_SESSION['selected_trip'], '<br>';
    echo json_encode($_SESSION['trip']), '<br>';
    echo json_encode($_SESSION['min']), '<br>';
    echo json_encode($_SESSION['max']), '<br>';
    echo json_encode($_SESSION['settings']), '<br>';
?>