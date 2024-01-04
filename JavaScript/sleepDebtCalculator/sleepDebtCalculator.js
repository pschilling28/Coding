const getSleepHours = day => {
    switch (day) {
        case 'monday':
            return 7;
            break;
        case 'tuesday' :
            return 6;
            break;
        case 'wednesday' :
            return 7;
            break;
        case 'thursday' :
            return 7;
            break;
        case 'friday' :
            return 6;
            break;
        case 'saturday' :
            return 6;
            break;
        case 'sunday' :
            return 8;
            break;
    }
};

//console.log(getSleepHours('sunday'));

const getActualSleepHours = () => 7 + 6 + 7 + 7 + 6 + 6 + 8;

const getIdealSleepHours = idealHoursPerNight => {
    return idealHoursPerNight * 7;
};

//console.log(getActualSleepHours());
//console.log(getIdealSleepHours());

const calculateSleepDebt = () => {
    const actualSleepHours = getActualSleepHours();
    const idealSleepHours = getIdealSleepHours(7);
    if (actualSleepHours === idealSleepHours) {
        console.log('You got the perfect amount of sleep!');
    } else if (actualSleepHours < idealSleepHours) {
        console.log(`You did not get enough sleep. You have a sleep debt of ${idealSleepHours - actualSleepHours} hours.`);
    } else {
        console.log(`You got enough sleep! You passed your ideal sleep hours by ${actualSleepHours - idealSleepHours} hours. Just don't sleep in too much, you lazy bum.`);
    }
};

calculateSleepDebt();