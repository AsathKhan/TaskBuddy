function displayGreeting(){
    const greetingElement = document.getElementById('greeting');
    const hour = new Date().getHours();
    let greetingText = "welcome";

    if (hour<12){
        greetingText = "Good Morning";
    }
    else if(hour<18){
        greetingText = "Good Afternoon";
    }
    else{
        greetingText = "Good Evening";
    }

    greetingElement.textContent = `${greetingText}, ${greetingElement.dataset.username}!`;
}
displayGreeting();