/* eslint-disable no-new-object */
/* eslint-disable no-array-constructor */
import CallType from './callType';
/**
 * CallHistory obj structure
 * CallHistory obj {
 *   history obj {
 *     ph1_str obj {
 *       allCallsArray = [contains all callLog objects]
 *       name = name
 *       phoneNumber = phoneNumber
 *       duration = num
 *       callType: {
 *       }
 *     }
 *     ph2_str {
 *     }
 *   }
 * }
 * */
export default class CallGrouping {

  constructor(call) {
    this.groupingType = call.groupingType;
    this.key = call.key;
    this.callType = new CallType();
    this.duration = 0;
    
  }
}
