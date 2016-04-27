
function styleNavbarElement() {
    var parts = window.location.search.substr(1).split("&");
    var $_GET = {};
    for (var i = 0; i < parts.length; i++) {
        var temp = parts[i].split("=");
        $_GET[decodeURIComponent(temp[0])] = decodeURIComponent(temp[1]);
    }

    var list_id = $_GET['data'];
    console.log(typeof list_id);
    if (typeof list_id != 'string') {
        document.getElementById('main').style.backgroundColor = "#333333";
    } else {
        document.getElementById(list_id).style.backgroundColor = "#333333";
    }
}

window.onload = styleNavbarElement;