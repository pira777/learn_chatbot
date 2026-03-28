function sendMessage(){
    let msg = document.getElementById("userInput").value;

    fetch(`/api/chat/?message=${encodeURIComponent(msg)}`)
        .then(response => response.json())
        .then(data => {document.getElementById("reply").innerText= data.reply;});
}