let input = 'Turpentine and turtles';

const vowels = ['a', 'e', 'i', 'o', 'u'];

let resultArray = [];

for (let i = 0; i < input.length; i++) {
    input = input.toLowerCase();
    if (input[i] === 'e' || input[i] === 'u') {
        resultArray.push(input[i]);
    };
    //console.log(i);
    for (let j = 0; j < vowels.length; j++) {
        //console.log(j);
        if (vowels[j] === input[i]) {
            //console.log(vowels[j]);
            resultArray.push(vowels[j]);
        };
    };
};

let resultString = resultArray.join('').toUpperCase();
console.log(resultString);
