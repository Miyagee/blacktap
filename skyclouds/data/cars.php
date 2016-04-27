<html>
   
   <head>
      <title>Cars</title>
   </head>
   
   <body>
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
					. " '" . $car_manufactor_type . "'"
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
				"<div style='left:50px; top:20px; position:relative;'>
				<table border='1'>
					<col width='130'>
					<col width='130'>
					<col width='130'>
					<col width='130'>
					<col width='130'>
					<thread>
						<tr style='cursor:pointer; color:blue;'>
							<th id='carid'>Car Identification</th>
							<th id='reg'>Registration Number</th>
							<th id='date'>Date Purchased</th>
							<th id='car'>Car Brand</th>
							<th id='fuel'>Fuel Tank Size</th>
						</tr>
					</thread>
					<tbody id='carTable'>"
			);
			
			foreach($data as $key => $value) {
				echo "<tr>";
				foreach($data[$key] as $new_key => $new_value) {
					echo "<td>" . $new_value . "</td>";
				}
				echo "</tr>";
			}
			
			echo ("</tbody></table></div>");
			echo ("<script src='js/sortTable.js'></script>");
		?>
   </body>
</html>