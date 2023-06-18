let raceNumber = Math.floor(Math.random() * 1000);

let early = true;

let runnerAge = 18;

if (runnerAge > 18 && early) {
    raceNumber += 1000;
}

if (runnerAge > 18 && early) {
    console.log(`Racer number ${raceNumber}, you will race at 09:30.`);
} else if (runnerAge > 18 && !early) {
    console.log(`Racer number ${raceNumber}, you will race at 11:00.`);
} else if (runnerAge < 18) {
    console.log(`Racer number ${raceNumber}, youth registrants run at 12:30 pm (regardless of registration time).`);
} else {
    console.log('Please see the registration desk. Thank you.');
}
