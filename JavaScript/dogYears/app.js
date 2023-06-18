//Setting my age variable
let myAge = 69;

//Setting variable for different counting behavior for first two years
let earlyYears = 2;

earlyYears *= 10.5;

//Removing two years from age to acount for rest of the math
let laterYears = myAge - 2;

//Each year after the first two use a factor of four
laterYears *= 4;

/* test 
console.log(earlyYears);
console.log(laterYears);
*/

//Sums both results to equal end result
myAgeInDogYears = earlyYears + laterYears;

//Creating name variable and lower-casing it
const myName = 'Pat Schilling'.toLowerCase();

//Output text
console.log(`My name is ${myName}. I am ${myAge} years old in human years which is ${myAgeInDogYears} years old in dog years.`)