<?php

	$username = "skyclouds_admin"; 
	$password = "blacktap";   
	$host = "mysql.stud.ntnu.no";
	$database="skyclouds_blacktap";
	
	$server = mysql_connect($host, $username, $password);
	$connection = mysql_select_db($database, $server);

?>