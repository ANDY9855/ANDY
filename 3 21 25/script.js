function openModal(message, isPrompt = false) {
    document.getElementById("message").innerText = message;
    let inputBox = document.getElementById("inputBox");

    if (isPrompt) {
        inputBox.style.display = "block";  // Show input box for prompt
    } else {
        inputBox.style.display = "none";  // Hide input box for alert messages
    }

    document.getElementById("modal").style.display = "block";
    document.getElementById("overlay").style.display = "block";
}

function closeModal() {
    document.getElementById("modal").style.display = "none";
    document.getElementById("overlay").style.display = "none";
}

function dare() {
    openModal("Tell me a secret 😁", true);
}

function truth() {
    openModal("You are not an alien 😎");
}
