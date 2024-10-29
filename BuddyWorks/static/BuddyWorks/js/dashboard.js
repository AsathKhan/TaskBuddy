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


function setupTabs(){
    const tabs = document.querySelectorAll(".tab");
    const contents = document.querySelectorAll('.tab-content');

    tabs.forEach((tab, index) =>{
        tab.addEventListener("click", ()=> {
            //removes "active" class from all buttons
            tabs.forEach(t => t.classList.remove("active"));
            //hides all contents
            contents.forEach(content => content.classList.add("hidden"));
    
            //only add "active" to clicked button
            tab.classList.add('active');
            contents[index].classList.remove("hidden");
        });
    });
}


function setupToggles(){
    const toggleButtons = document.querySelectorAll('.toggle-button');

    toggleButtons.forEach(toggleButton => {
        toggleButton.addEventListener('click', () =>{
            const targetContent = document.querySelector(toggleButton.dataset.target);

            targetContent.classList.toggle("hidden");
        });
    });
}


displayGreeting();
setupTabs();
setupToggles();