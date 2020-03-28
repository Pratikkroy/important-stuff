
const month = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'
};
export default class DateTime{

    static convertSecondsToMinutes(seconds){
        return {
            minutes: parseInt(seconds/60),
            seconds: parseInt(seconds%60)
        }
    }

    static getTodayDate(){
        let todayDate = new Date();
        return todayDate.getDate() + ' ' + 
        month[todayDate.getMonth()]+ ' ' + 
        todayDate.getFullYear();
    }
}