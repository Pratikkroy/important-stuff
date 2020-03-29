
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

    static getLastSunday(date){
        let todayDate = new Date(date.getFullYear(), date.getMonth(), date.getDate(), 0, 0, 0, 0);
        todayDate.setDate(date.getDate()-date.getDay())
        return todayDate;
    }

    static getNextSunday(date){
        let todayDate = new Date(date.getFullYear(), date.getMonth(), date.getDate(), 0, 0, 0, 0);
        todayDate.setDate(todayDate.getDate()+(7-date.getDay()))
        return todayDate;
    }

    // returns date in the form dd-mm-yyyy
    static convertTimestampToDate(timestamp){
        let date = new Date(timestamp);
        return date.getDate().toString()+'-'+month[date.getMonth()+1]+'-'+date.getFullYear();
    }

    // returns date in the form dd-mm-yyyy
    static convertDateObjToDate(date){
        return date.getDate().toString()+'-'+month[date.getMonth()+1]+'-'+date.getFullYear();
    }
}