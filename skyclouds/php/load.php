
<!-- 
Filnavn: php/load.php
Skrivd av: Kevin Midboe
Når: November 2015
Mening med siden: Gir ut en feilmelding hvis fagsiden ikke finnes. 
-->


<?php
	
	// Her blir fagkode fra urlen lagret i fag_kode
	$fag_kode = $_GET['data'];
	// Her lager vi filnavnet i en variabel
	$file_name = 'data/' . $fag_kode . '.php';

	// Her sjekkes det om filen eksisterer
	if ($_SERVER['REQUEST_URI'] === '/skyclouds/main.php'){
		include 'data/dashboard.php';
	} else if(file_exists($file_name)){
		// Hvis den gjør det, blir den importert inn i siden
		include $file_name;
	} else {
		// Melding om at filen ikke finnes
		echo '<h1>404 File not found</h1>';
		$imagename = 400 + fmod(mt_rand(), 3);
		echo '<img src="images/' . $imagename . '.gif">';
	}
?>
