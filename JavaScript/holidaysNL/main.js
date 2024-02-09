/* rules
    - there are two types of holidays, legal and bovenwettelijke vakantiedagen, each with different expiration lengths (ex leg 6mos into next year, bv 5yrs)
    - 20 legal holidays award per year, 10 personal
    - 10 holidays can be carried over, but they need to be earmarked which kind of holidays (ex 6 leg 4 bv)
    - there is a priority to which holidays are used first in a holiday bank (oldest holidays used first)
    - there is a priority which holidays are carried over first to the next year (ex must carry over all leg before any pers)
    - everyone has a right to 4x weekly contract hours in holiday, and can be taken in hours
*/

const coworker = (id, hours, startDate) => {
    return {
        coworkerId: id,
        contractHours: hours,
        contractStart: startDate,
        legalHolidayAnnual: 5 * hours,
        holidayAccrued: [{type: 'legal', balance: 5 * hours, date: startDate}],
        accrueHoliday(type, date) {
            if (type !== 'legal' && type !== 'bv') {
                console.log('Holiday type is not valid.');
            }
            if (type === 'legal') {
                this.holidayAccrued.unshift({type:'legal', balance: this.legalHolidayAnnual, date});
            }
            if (type === 'bv') {
                this.holidayAccrued.unshift({type: 'bv', balance : this.contractHours / 5, date});
            }
        },
        useHoliday(hours) {
            
        }
    }
}


//testing
let himari = coworker(39991253, 38, '2021-01-04');
console.log(himari);
himari.accrueHoliday('bv', '2024-02-09');
console.log(himari);
//himari.useHoliday(8);