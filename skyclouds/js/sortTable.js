window.addEventListener('load', afterLoad);

function afterLoad() {
	arr = getArray();
	document.getElementById("carid").addEventListener('click', function() {
		arr = sorter(arr, 0);
		updateTable(arr);
	});
	document.getElementById("reg").addEventListener('click', function() {
		arr = sorter(arr, 1);
		updateTable(arr);
	});
	document.getElementById("date").addEventListener('click', function() {
		arr = sorter(arr, 2);
		updateTable(arr);
	});
	document.getElementById("car").addEventListener('click', function() {
		arr = sorter(arr, 3);
		updateTable(arr);
	});
	document.getElementById("fuel").addEventListener('click', function() {
		arr = sorter(arr, 4);
		updateTable(arr);
	});
}

function updateTable(arr) {
	for (x = 0; x < rows.length; x++) {
		rows[x].innerHTML = "<td>" + arr[x].join("</td><td>") + "</td>";
	}
}

function getArray() {
	tbody = document.getElementById("carTable");
	rows = tbody.rows;
	arr = new Array();

	for(x = 0; x < rows.length; x++) {
		cells = rows[x].cells;
		arr[x] = new Array();
		for(z = 0; z < cells.length; z++) {arr[x][z] = cells[z].innerHTML;}
	}
	return arr;
}

function sorter(arr, col) {
	arr.sort(function(a ,b) {
		if(a[col] > b[col]) {
			return 1;	
		}
		return -1;		
	});
	return arr;
}