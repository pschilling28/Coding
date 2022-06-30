const _ = {
    /*clamp(num, lo, hi) {
        if (num >= lo && num <= hi) {
            return num;
        } else if (num < lo) {
            return lo;
        } else {
            return hi;
        };
    },*/
    clamp(number, lower, upper) {
        let lowerClampedValue = Math.max(number, lower);
        let clampedValue = Math.min(lowerClampedValue, upper);
        return clampedValue;
    },
    inRange(number, lower, upper) {
        if (upper === undefined) {
            upper = lower;
            lower = 0;
            //console.log(`${lower}, ${upper}`);
        };
        if (upper < lower) {
            [upper, lower] = [lower, upper];
            //console.log(`${lower}, ${upper}`);
        };
        //console.log(`${number}, ${lower}, ${upper}`);
        if (number >= lower && number < upper) {
            return true;
        } else {
            return false;
        };
    },
    words(string) {
        return string.split(' ');
    },
    pad(string, length) {
       if (length <= string.length) {
           return string;
       }
       let padStart = Math.floor((length - string.length)/2);
       let padEnd = length - string.length - padStart;
       let paddedString = ' '.repeat(padStart).concat(string).concat(' '.repeat(padEnd));
       return paddedString;
    },
    has(object, key) {
        if (object[key]) {
            return true;
        } else {
            return false;
        };
    },
    invert(object) {
        let invertedObject = {};
        for (let key in object) {
            const originalValue = object[key];
            invertedObject = {originalValue : key};
        };
        return invertedObject;
    },
    findKey(object, predicate) {
        for(let key in object) {
            if (predicate(object[key]) === true) {
                return key;
            }
            return undefined;
        };
    },
    drop(arr, num) {
        if (num === undefined) {
            num = 1;
        };
        let arr2 = arr.slice(num);
        return arr2;
    },
    dropWhile(arr, predicate) {
        
    },
};


//test code area
console.log(_.clamp(1, 5, 10)); // [5]
console.log(_.clamp(6, 5, 10)); // [6]
console.log(_.clamp(11, 5, 10)); // [10]
console.log(_.inRange(1, 5, 10)); // [false]
console.log(_.inRange(6, 5, 10)); // [true]
console.log(_.words('Hello, my name is Pat.')); // ['Hello,', 'my', 'name', 'is', 'Pat.']
console.log(_.pad('Pat', 2)); // [Pat]
console.log(_.pad('Pat', 9)); // [   Pat   ]

// Do not write or modify code below this line.
module.exports = _;