const chatForm = document.getElementById('chat-box');
const formMessages = document.getElementById("form-messages")

chatForm.addEventListener('submit', (e) =>{ 

    const username = document.getElementById('username').value.trim();
    const email = document.getElementById("email").value.trim();
    const message = document.getElementById('message').value.trim();

    if (username == "" || email ==="" || message === ""){
        // we used *required in input. so no use of this if block
        alert("please fill out all fields", "error");

    }else{
        alert("Message sent! Our Support team will get back to you shortyly!", 'success');
        chatForm.reset();
    }
});
