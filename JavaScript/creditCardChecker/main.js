// All valid credit card numbers
const valid1 = [4, 5, 3, 9, 6, 7, 7, 9, 0, 8, 0, 1, 6, 8, 0, 8];
const valid2 = [5, 5, 3, 5, 7, 6, 6, 7, 6, 8, 7, 5, 1, 4, 3, 9];
const valid3 = [3, 7, 1, 6, 1, 2, 0, 1, 9, 9, 8, 5, 2, 3, 6];
const valid4 = [6, 0, 1, 1, 1, 4, 4, 3, 4, 0, 6, 8, 2, 9, 0, 5];
const valid5 = [4, 5, 3, 9, 4, 0, 4, 9, 6, 7, 8, 6, 9, 6, 6, 6];

// expect for valid3 holderArr: 3 5 1 3 1 4 0 2 9 9 8 1 2 6 6

// All invalid credit card numbers
const invalid1 = [4, 5, 3, 2, 7, 7, 8, 7, 7, 1, 0, 9, 1, 7, 9, 5]; //Visa
const invalid2 = [5, 7, 9, 5, 5, 9, 3, 3, 9, 2, 1, 3, 4, 6, 4, 3]; //Mastercard
const invalid3 = [3, 7, 5, 7, 9, 6, 0, 8, 4, 4, 5, 9, 9, 1, 4]; //Amex
const invalid4 = [6, 0, 1, 1, 1, 2, 7, 9, 6, 1, 7, 7, 7, 9, 3, 5]; //Discover
const invalid5 = [5, 3, 8, 2, 0, 1, 9, 7, 7, 2, 8, 8, 3, 8, 5, 4]; //Mastercard

// Can be either valid or invalid
const mystery1 = [3, 4, 4, 8, 0, 1, 9, 6, 8, 3, 0, 5, 4, 1, 4]; //Amex
const mystery2 = [5, 4, 6, 6, 1, 0, 0, 8, 6, 1, 6, 2, 0, 2, 3, 9]; //valid
const mystery3 = [6, 0, 1, 1, 3, 7, 7, 0, 2, 0, 9, 6, 2, 6, 5, 6, 2, 0, 3]; //Discover
const mystery4 = [4, 9, 2, 9, 8, 7, 7, 1, 6, 9, 2, 1, 7, 0, 9, 3]; //Visa
const mystery5 = [4, 9, 1, 3, 5, 4, 0, 4, 6, 3, 0, 7, 2, 5, 2, 3]; //valid

// An array of all the arrays above
const batch = [valid1, valid2, valid3, valid4, valid5, invalid1, invalid2, invalid3, invalid4, invalid5, mystery1, mystery2, mystery3, mystery4, mystery5];


// Add your functions below:
const validateCred = arr => {
    let holderArr = [];
    for (let i = arr.length - 1; i >= 0; i = i-2) {
        holderArr[i] = arr[i];
        holderArr[i-1] = arr[i-1] * 2;
        if (holderArr[i-1] > 9) {
            holderArr[i-1] = holderArr[i-1] - 9;
        };
    }
    let holderArrSum = holderArr.reduce((a, b) => a + b);

    //test
    //console.log(holderArr);
    //console.log(arr);
    //console.log(holderArrSum);

    if (holderArrSum % 10 === 0) {
        return 'valid';
    } else {
        return 'invalid';
    }
}

const findInvalidCards = arr => {
    let invalidList = [];
    for (let i = 0; i < arr.length; i++) {
        if (validateCred(arr[i]) === 'invalid') {
            invalidList.push(arr[i]);
        }
    }
    return invalidList;
}

const idInvalidCardCompanies = arr => {
    companyArr = [];
    for (let i = 0; i < arr.length; i++) {
        switch (arr[i][0]) {
            case 3:
                companyArr.push('American Express');
                break;
            case 4:
                companyArr.push('Visa');
                break;
            case 5:
                companyArr.push('Mastercard');
                break;
            case 6:
                companyArr.push('Discover');
                break;
            default:
                companyArr.push('Company not found');
                break;
        };
    }
    return companyArr;
}

//test
//console.log(validateCred(valid1));
//console.log(findInvalidCards(batch));
//console.log(idInvalidCardCompanies(findInvalidCards(batch)));