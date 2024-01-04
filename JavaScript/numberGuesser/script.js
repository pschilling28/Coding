let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:



const generateTarget = () => {
    return Math.floor(Math.random() * 10);
};

const compareGuesses = (human, computer, target = 0) => {
    if (getAbsoluteDistance(target, human) <= getAbsoluteDistance(target, computer)) {
        console.log(`Human guess is ${human}. Computer guess is ${computer}. The correct number is ${target}. Human wins!`);
        return true;
    } else {
        console.log(`Human guess is ${human}. Computer guess is ${computer}. The correct number is ${target}. Computer wins!`);
        return false;
    };
};

const updateScore = winner => {
    if (winner === 'human') {
        humanScore++;
    } else {
        computerScore++;
    };
};

const advanceRound = () => {
    currentRoundNumber++;
};

const getAbsoluteDistance = (num1, num2) => {
    return Math.abs(num1 - num2);
};

// Test code below
//console.log(generateTarget());
//compareGuesses(5,0);
//updateScore();
