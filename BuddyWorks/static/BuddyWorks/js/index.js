const welcomeMessage = document.querySelector(".welcome h2");
const messages = [
    "Welcome to TaskBuddy!",
    "Manage Your Tasks Efficiently!",
    "Stay Organized with TaskBuddy!"
];
let messageIndex = 0;

setInterval(() => {
    welcomeMessage.textContent = messages[messageIndex];
    messageIndex = (messageIndex + 1) % messages.length;
},3000);