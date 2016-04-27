<?php

	$username = "skyclouds_admin"; 
	$password = "blacktap";   
	$host = "mysql.stud.ntnu.no";
	$database="skyclouds_blacktap";
	
	$server = mysql_connect($host, $username, $password);
	$connection = mysql_select_db($database, $server);
	
	$myquery = (
		"SELECT * FROM skyclouds_blacktap.settings WHERE idPerson EQUALS '" + $_SESSION[idPerson] + "'"
	);

	$query = mysql_query($myquery);

	if(!$query) {
        echo mysql_error();
        die;
    }
	/*
    $data = array();

    for($x = 0; $x < mysql_num_rows($query); $x++) {
        $data[] = mysql_fetch_assoc($query);
    }
	
	for($x = 0; $x < $data; $x++) {
		echo(
			"<input type="checkbox" name='" + $data[$x] + "' value='" + $data[$x] + "' > " + $data[$x] + " <br>"
		);
	}
	*/
?>