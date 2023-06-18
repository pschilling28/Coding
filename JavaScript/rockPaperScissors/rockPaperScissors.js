const getUserChoice = userInput => {
    userInput = userInput.toLowerCase();
    if (userInput === 'rock' || userInput === 'scissors' || userInput === 'paper' || userInput === 'bomb') {
        return userInput;
    } else {
        return `Pick a real answer, dummy. Does "${userInput}" look like rock, paper, or scissors to you?`;
    }
};

//console.log(getUserChoice('rock'));

const getComputerChoice = () => {
    if (Math.floor(Math.random() * 3) === 0) {
        return 'rock';
    } else if ((Math.floor(Math.random() * 3) === 1)) {
        return 'paper';
    } else {
        return 'scissors';
    }
};

//console.log(getComputerChoice());

const determineWinner = (userChoice, computerChoice) => {
    if (userChoice === 'bomb') {
        return `Player wins!`;
    }
    if (userChoice === computerChoice) {
        return `The result is a tie.`;
    }
    if (userChoice === 'rock') {
        if (computerChoice === 'scissors') {
            return `Player wins!`;
        } else {
            return `Computer wins!`;
        }
    }
    if (userChoice === 'scissors') {
        if (computerChoice === 'paper') {
            return `Player wins!`;
        } else {
            return `Computer wins!`;
        }
    }
    if (userChoice === 'paper') {
        if (computerChoice === 'rock') {
            return `Player wins!`;
        } else {
            return `Computer wins!`;
        }
    }
};

//console.log(determineWinner('paper', 'rock'));

const playGame = () => {
    const userChoice = getUserChoice('bomb');
    const computerChoice = getComputerChoice();
    console.log(`Player chose ${userChoice}.`);
    console.log(`Computer chose ${computerChoice}.`);
    console.log(determineWinner(userChoice, computerChoice));
};

playGame();