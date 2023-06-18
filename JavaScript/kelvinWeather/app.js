// Setting constant Kelvin factor
const kelvin = 0;
// Setting Celsius to be 273 degrees less than Kelvin constantly
const celsius = kelvin - 273;
// Setting Fahrenheit formula, including rounding down
let fahrenheit = Math.floor(celsius * (9/5) + 32);

console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`)
