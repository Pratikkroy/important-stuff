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

    static updateCallType(elementToBeUpdated, call){
        switch(call.rawType){
            case 1:
              elementToBeUpdated.callType.INCOMING += 1;
              break;
            case 2:
              if(call.duration === 0){
                elementToBeUpdated.callType.NOT_ANSWERED += 1;
              } else {
                elementToBeUpdated.callType.OUTGOING += 1;
              }
              break;
            case 3: 
              elementToBeUpdated.callType.MISSED += 1;
              break;
            default: 
              elementToBeUpdated.callType.UNKNOWN += 1;
        }
    }

    
    
}