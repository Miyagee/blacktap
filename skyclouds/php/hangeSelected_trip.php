<?php
	Session_Start();

	$_SESSION['selected_trip'] = $_POST['data'];

	echo "<script type='text/javascript'>console.log('gs');</script>";
?>