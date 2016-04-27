<!--
	FILE NAME:	logged_in_test.php
	WRITTEN BY:	Aage Johansen
	WHEN:		February 2016
	PURPOSE:	Check if user is logged in when entering index.php, redirect to home if they are
-->

<?php
	Session_Start();
	if(isset($_SESSION['login_user'])){ // OR isset($_SESSION['user']), if array
	/*
		define('DB_NAME', 'skyclouds_blacktap');
    	define('DB_USER', 'skyclouds_admin');
    	define('DB_PASSWORD', 'blacktap');
    	define('DB_HOST', 'mysql.stud.ntnu.no');
    */
    	require_once 'php/conn.php';
		// Setter brukernavn og passord hentet fra logg_inn.

		// Kobler til databasen.
		$connection = mysql_connect($hn, $un, $pw);
		// Sikkerhet for å beskytte fra mysql injections.

		// Velger database.
		mysql_select_db($nm, $connection);

		if ($row['type'] == "bruker"){
			$query = mysql_query("SELECT tripId, MIN(timestamp) as 'min', MAX(timestamp) as 'max' from data WHERE bil_idBil = (SELECT bil_idBil from person INNER JOIN bruker ON person.idPerson = bruker.id INNER JOIN login ON bruker.login_idLogin = login.idLogin AND bruker.login_type = login.type WHERE login.brukernavn = '$username') GROUP BY tripId", $connection);

			$trip = array();
			$min = array();
			$max = array();
			while($row =  mysql_fetch_assoc($query)){
					$trip[] = intval($row['tripId']);
					$min[] = $row['min'];
					$max[] = $row['max'];
			}
			$_SESSION['trip'] = $trip;
			$_SESSION['min'] = $min;
			$_SESSION['max'] = $max;
			$_SESSION['selected_trip'] = end($trip);

			$query = mysql_query("SELECT * from settings WHERE brukernavn = '$username'", $connection);
			$settings[] = array();
			while($row = mysql_fetch_assoc($query)){
				
				$settings[0] = intval($row['speed']);
				$settings[1] = intval($row['reckless']);
				$settings[3] = intval($row['odometer']);
				$settings[2] = intval($row['fuel']);
				$settings[4] = intval($row['fuelLast']);
				$settings[5] = intval($row['maxLast']);
				$settings[6] = intval($row['avgLast']);
				$settings[7] = intval($row['mapLast']);
				$settings[8] = intval($row['distanceLast']);
			}
			$_SESSION['settings'] = $settings;
		} else if ($row["type"] == "forhandler"){

		} else if ($row["type"] == "produsent"){

		}
		header("location: main.php"); //Redirecter til logged inn side

		mysql_close($connection); // Closing Connection
	}
?>