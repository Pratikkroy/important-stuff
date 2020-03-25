/* eslint-disable no-new-object */
/* eslint-disable no-array-constructor */
import CallLog from './callLog';

/**
 * CallHistory obj structure
 * CallHistory obj {
 *   history obj {
 *     ph1_str obj {
 *       allCallsArray = [contains all callLog objects]
 *       name = name
 *       phoneNumber = phoneNumber
 *       duration = num
 *     }
 *     ph2_str {
 *     }
 *   }
 * }
 * */
export default class CallHistory {
  constructor(callLogData) {
    this.history = new Object();
    callLogData.map(callLog => {
      var phoneNumber = this.getPrefixAndPhoneNumber(callLog.phoneNumber);
      if (!this.history[phoneNumber.phoneNumber]) {
        let _newEntry = new Object();
        _newEntry.allCallsArray = new Array();
        _newEntry.name = callLog.name;
        _newEntry.phoneNumber = phoneNumber.phoneNumber;
        _newEntry.duration = 0;
        this.history[phoneNumber.phoneNumber] = _newEntry;
      }
      this.history[phoneNumber.phoneNumber].allCallsArray.push(
        new CallLog(
          callLog.id,
          phoneNumber.phoneNumber,
          phoneNumber.prefix,
          callLog.type,
          callLog.duration,
          callLog.timestamp,
          callLog.dateTime,
        ),
      );
      this.history[phoneNumber.phoneNumber].duration += callLog.duration;
    });
  }

  getPrefixAndPhoneNumber(phoneNumber) {
    if (phoneNumber.startsWith('+91')) {
      return {
        prefix: '+91',
        phoneNumber: phoneNumber.substring(3, phoneNumber.length),
      };
    } else if (phoneNumber.length === 12 && phoneNumber.startsWith('91')) {
      return {
        prefix: '91',
        phoneNumber: phoneNumber.substring(2, phoneNumber.length),
      };
    } else if (phoneNumber.length === 11 && phoneNumber.startsWith('0')) {
      if (phoneNumber.startsWith('011')) {
        return {
          prefix: '011',
          phoneNumber: phoneNumber.substring(3, phoneNumber.length),
        };
      } else if (phoneNumber.startsWith('012')) {
        return {
          prefix: '012',
          phoneNumber: phoneNumber.substring(3, phoneNumber.length),
        };
      } else {
        return {
          prefix: '0',
          phoneNumber: phoneNumber.substring(1, phoneNumber.length),
        };
      }
    } else {
      return {
        prefix: null,
        phoneNumber: phoneNumber,
      };
    }
  }

  getCallHistoryArray(){
    let callHistoryArr = [];
    for (let [key, value] of Object.entries(this.history)) {
      callHistoryArr.push(value);
    }
    return callHistoryArr;
  }
}
