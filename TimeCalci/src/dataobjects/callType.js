export default class CallType {
    INCOMING;
    OUTGOING;
    MISSED;
    
    NOT_ANSWERED;
    UNKNOWN;

    constructor() {
        this.MISSED = 0;
        this.INCOMING = 0;
        this.OUTGOING = 0;
        this.NOT_ANSWERED = 0;
        this.UNKNOWN = 0;
    }
}