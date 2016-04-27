<?php
/*
Filnavn: php/logout.php
Skrivd av: Aage Johansen, Kevin Midboe
Når: April 2016
Mening med siden: Logge ut fra nettsiden og kutte session.
*/

session_start();
if(session_destroy()) // Kutter alle connections.
{
	header("Location: ../index.php"); //Redirecter til hovedsiden.
}
?>
