<!--
	FILE NAME:	login.php
	WRITTEN BY:	Kevin Midbøe
	WHEN:		February 2016
	PURPOSE:	Handles login by checking if the credentials exists in the db. 
				Redirects to sidebar/sidebar.php
-->

<?php
	session_Start();

$error=''; // Variabel for å lagre feilmelding.
if (isset($_POST['submit'])) {
	if (empty($_POST['username']) || empty($_POST['password'])) {
		$error = "Username or Password is invalid";
	}
	else
	{
		define('DB_NAME', 'skyclouds_blacktap');
    	define('DB_USER', 'skyclouds_admin');
    	define('DB_PASSWORD', 'blacktap');
    	define('DB_HOST', 'mysql.stud.ntnu.no');
		// Setter brukernavn og passord hentet fra logg_inn.
		$username=$_POST['username'];
		$password=$_POST['password'];

		// Kobler til databasen.
		$connection = mysql_connect(DB_HOST, DB_USER, DB_PASSWORD);
		// Sikkerhet for å beskytte fra mysql injections.
		$username = stripslashes($username);
		$password = stripslashes($password);
		$username = mysql_real_escape_string($username);
		$password = mysql_real_escape_string($password);

		// Velger database.
		mysql_select_db(DB_NAME, $connection);
		// SQL setning som henter info om psw og brukernavn.
		$query = mysql_query("SELECT type FROM login WHERE passord='$password' AND brukernavn='$username' LIMIT 1", $connection);
		$rows = mysql_num_rows($query);
		$row = mysql_fetch_assoc($query);

		if ($rows == 1) {
			$_SESSION['login_user'] = $username; // Laster session.
			$_SESSION['type'] = $row["type"];
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
					$settings[2] = intval($row['fuel']);
					$settings[3] = intval($row['odometer']);
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
		}else {
			$error = "Username or Password is wrong";
		}
		mysql_close($connection); // Closing Connection
	}
}
?>