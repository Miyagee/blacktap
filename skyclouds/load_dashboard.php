<?php 
	session_start();

	$settings_array = array('data/speed.php', 'reckless', 'data/odometer.php', 'data/fuel_left.php', 'data/fuel_usage.php', 'maxLast', 'avgLast', 'data/trip_map.php', 'lasf');


	$user_settings = $_SESSION['settings'];


	$super_x = 0;
	foreach ($user_settings as $settingValue) {
		if ($settingValue == 1) {
			if ($super_x == 6) {
				echo "<h1>Map:</h1><br>";
			}
			include $settings_array[$super_x];
		}
		$super_x = $super_x+1;
	}
 ?>