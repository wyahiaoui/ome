
function get_ip() {
    fetch("http://localhost:8080/", {
        method: "POST",
        headers: {'Content-Type': 'application/json'}
    }).then(res => {
        console.log("Request complete! response:", res);
        return res.json()
    }).then((data) => {
        console.log("DATA", data);
        document.getElementById("test").innerText = JSON.stringify(data);
    });
}

var intervalId = setInterval(get_ip, 2500);
