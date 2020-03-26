
export default class DateTime{

    static convertSecondsToMinutes(seconds){
        return {
            minutes: parseInt(seconds/60),
            seconds: parseInt(seconds%60)
        }
    }
}