<?php 
	
	Session_start();

    if($_SESSION['type'] == 'bruker'){
        echo
    '<li class="sidebar-brand">
        <a href="main.php">
            BlackTap
        </a>
    </li>
    <li id="main">
        <a href="main.php">Dashboard</a>
    </li>
    <li id="car">
        <a href="main.php?data=car">Car info</a>
    </li>
    <li id="reckless">
      <a href="map.php">Reckless</a>
    </li>
    <li id="fuel_usage">
        <a href="main.php?data=fuel">Gas mileage</a>
    </li>
    <li id="trip_map">
        <a href="main.php?data=trip_map">Trip map</a>
    </li>
    <li id="speed">
        <a href="main.php?data=speed">Speed</a>
    </li>
    <li id="odometer">
        <a href="main.php?data=odometer">Odometer</a>
    </li>
    <li id="misc">
        <a href="main.php?data=misc">Misc</a>
    </li>
    <li id="settings">
      <a href="main.php?data=settings">Settings</a>
    </li>
    <li>
        <br>
    </li>
    <li>
        <div>
        <span>Trip</span>';
            include "php/combobox_trip.php";
    echo
        '</div>
    </li>';
     } else if($_SESSION['type'] == 'forhandler'){
        echo
        '<li class="sidebar-brand">
            <a href="main.php">
                BlackTap
            </a>
        </li>
        <li id="car">
            <a href="main.php?data=cars">Car</a>
        </li>';
     } else if($_SESSION['type'] == 'produsent'){
     	echo 
        '<li class="sidebar-brand">
            <a href="main.php">
                BlackTap
            </a>
        </li>
        <li id="car">
            <a href="main.php?data=cars">Car</a>
        </li>';
     } else {
     	echo "mordi";
     }
?>