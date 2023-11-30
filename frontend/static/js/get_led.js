function get_led() {
    // Define la nueva URL
    const newURL = "https://git.heroku.com/iot-esp32.git";

    var request = new XMLHttpRequest;
    request.open('GET', newURL);
    request.send();

    request.onload = () => {
        const response = request.responseText;
        const json = JSON.parse(response);
        console.log("response: " + response);
        console.log("json: " + json);
        console.log("status_code: " + request.status);
        for (var i = 0; i < Object.keys(json).length; i++) {
            console.log(i);
        }
    };
}
