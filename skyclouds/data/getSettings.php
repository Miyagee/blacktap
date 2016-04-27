<?php

	$username = "skyclouds_admin"; 
	$password = "blacktap";   
	$host = "mysql.stud.ntnu.no";
	$database="skyclouds_blacktap";
	
	$server = mysql_connect($host, $username, $password);
	$connection = mysql_select_db($database, $server);

	
	$myquery = (
		"SELECT *
		FROM skyclouds_blacktap.settings
		WHERE brukernavn = '" . $_SESSION['login_user'] . "'"
	);
	
	$query = mysql_query($myquery);

	if(!$query) {
        echo mysql_error();
        die;
    }
	
    $data = array();

    for($x = 0; $x < mysql_num_rows($query); $x++) {
        $data[] = mysql_fetch_assoc($query);
    }
	
	foreach($data[0] as $key=>$value) {
		if($key != 'brukernavn') {
			if($value == 1) {
				echo(
					"<input type='checkbox' name='" . $key . "' value='" . $key . "' checked>" . ucfirst($key) . "<br>"
				);
			} else {
				echo(
					"<input type='checkbox' name='" . $key . "' value='" . $key . "'>" . ucfirst($key) . "<br>"
				);
			}
		}
	}

?>