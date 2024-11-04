let playerScore = 0;
let computerScore = 0;

function getComputerChoice(){
    const choices = ['🪨', '🧻', '✂️'];
    const randomIndex = Math.floor(Math.random() * choices.length);
    return choices[randomIndex];
};

function determineWinner(playerChoice, computerChoice) {
    if (playerChoice === computerChoice) {
        return "It's a tie!";
    }

    else if (
        (playerChoice === '🪨' && computerChoice === '✂️') ||
        (playerChoice === '🧻' && computerChoice === '🪨') ||
        (playerChoice === '✂️' && computerChoice === '🧻')
    ) {
        playerScore++;
        return 'You win!';
    } 
    
    else {
        computerScore++;
        return 'Computer wins!';
    }
};

function handlePlayerChoice(playerChoice) {
    const computerChoice = getComputerChoice();

    document.getElementById('playerDisplay').textContent = `PLAYER: ${playerChoice}`;
    document.getElementById('computerDisplay').textContent = `COMPUTER: ${computerChoice}`;

    const result = determineWinner(playerChoice, computerChoice);
    document.getElementById('resultDisplay').textContent = result;

    document.getElementById('playerScoreDisplay').textContent = playerScore;
    document.getElementById('computerScoreDisplay').textContent = computerScore;

    document.getElementById('resultDisplay').style.color =
        result === 'You win!' ? '#76e5fa' : result === 'Computer wins!' ? '#f28d8d' : '#ffdf00';
};


Btn = document.querySelectorAll('.choices button')

Btn.forEach(button => {
    button.addEventListener('click', () => {
        handlePlayerChoice(button.textContent);
    });
});
