<?php
	include 'car_by_type.php';
	
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
		for($z = 0; $z < sizeif($data[$x]); $z++) {
			echo("<td>" + $data[$x][$z] + "</td>");
		}
		echo("</tr>");
	}
	echo ("</table>");
	echo ("<script src="sortTable.js"></script>");
?>