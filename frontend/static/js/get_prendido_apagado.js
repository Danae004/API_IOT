function on_off(valor) {
    alert("Actualizar Led ");
    
    // Define las nuevas variables
    const id = 1;
    const dispositivo = "LED";
    const URL = `https://git.heroku.com/iot-esp32.git/${id}`;

    var request = new XMLHttpRequest;
    request.open('PUT', URL + "/" + valor, true);
    request.setRequestHeader("Content-Type", "application/json");
    
    // Usa las nuevas variables en el objeto JSON
    data = JSON.stringify({
        "id": id,
        "dispositivo": dispositivo,
        "valor": valor
    });

    request.send(data);

    request.onload = (e) => {
        const response = request.responseText;
        const json = JSON.parse(response);
        console.log(json);
        console.log("status_code: " + request.status);
        window.location.href = "../templates/index.html";
    };
}

