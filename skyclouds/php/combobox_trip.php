<?php 
	Session_Start();

	$i = 0;
	$len = count($array);
	echo '<form action="post"><select name="drop_2" id="drop_2" onchange="handleClick()">';
		   foreach($_SESSION['trip'] as $index => $tripId){
		   		if($tripId == $_SESSION['selected_trip']){
		   			echo '<option value=' . $tripId . ' selected>' . $_SESSION['min'][$index] . '</option>';
		   			// $_SESSION['selected_trip'] = $tripId;
		   		} else {
		   			echo '<option value=' . $tripId . '>' . $_SESSION['min'][$index] . '</option>';
		   		}
		   		$i++;
		   }
	echo '</select></form>';

	echo <<<END
	<span id="selectedText" style="display: none;"></span>
	<script type="text/javascript">
		function handleClick() {
			request = $.ajax({
			    type: 'POST',
			    url: 'php/changeSelected_trip.php',
			    dataType: 'html',
			    data: {
			        'data' : document.getElementById('drop_2').value,
			    }
			});

		// callback handler that will be called on success
		request.done(function (response, textStatus, jqXHR){
		    // log a message to the console
		    console.log("Hooray, it worked!");
		});
			location.reload();
		}
	</script>

END;

?>