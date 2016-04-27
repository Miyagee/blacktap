<?php
	
	Session_start();
	
	$username = "skyclouds_admin"; 
	$password = "blacktap";   
	$host = "mysql.stud.ntnu.no";
	$database="skyclouds_blacktap";
	
	$server = mysql_connect($host, $username, $password);
	$connection = mysql_select_db($database, $server);
	
	//$car_manufactor_type = $_SESSION['carType'];
	$car_manufactor_type = "mazda";
	
	$myquery = (
			"SELECT * FROM skyclouds_blacktap.bil WHERE bilmerke LIKE"
			. "'" . $car_manufactor_type . "'"
			. ";"
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
	
	echo(
		"<table id='carTable'>
			<tr>
				<th id='carid'>Car ID</th>
				<th id='reg'>Reg. Number</th>
				<th id='date'>P Date</th>
				<th id='car'>Car Type</th>
				<th id='fuel'>Fuel Tank</th>
			</tr>"
	);

	for($x = 0; $x < sizeof($data); $x++) {
		echo("<tr>");
		for($z = 0; $z < sizeof($data[$x]); $z++) {
			echo("<td>" + $data[$x][$z] + "</td>");
		}
		echo("</tr>");
	}
	
	echo ("</table>");
	//echo ("<script src="sortTable.js"></script>");
?>