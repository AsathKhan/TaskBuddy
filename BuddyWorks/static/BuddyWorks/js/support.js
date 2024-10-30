const chatForm = document.getElementById('chat-box');

chatForm.addEventListener('submit', (e) =>{
    e.preventDefault(); 

    const username = document.getElementById('username').value.trim();
    const message = document.getElementById('message').value.trim();

    if (username == "" || message === ""){
        alert("please fill out both your name and message.");
    }else{
        alert("Message sent! Our Support team will get back to you shortyly!");
        chatForm.reset();
    }
})