<!--
	FILE NAME:	login_test.php
	WRITTEN BY:	Aage Johansen
	WHEN:		February 2016
	PURPOSE:	Check if user is logged in, redirect to login if not
-->

<?php
	Session_Start();
	if(!isset($_SESSION['login_user'])){ // OR isset($_SESSION['user']), if array
		header("location: index.php"); //Redirecter til logged inn 
	}
?>