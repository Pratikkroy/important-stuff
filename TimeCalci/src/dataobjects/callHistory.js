/* eslint-disable no-new-object */
/* eslint-disable no-array-constructor */
import CallLog from './callLog';
import CallType from './callType';
import {blockedContacts} from '../config/blockedContacts';
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
export default class CallHistory {

  constructor(callLogData) {
    this.history = new Object();
    
    // adding map(js obj) of call history with 
    // phoneNumber as key
    callLogData.map(callLog => {
      var phoneNumber = this.getPrefixAndPhoneNumber(callLog.phoneNumber);
      if (!this.history[phoneNumber.phoneNumber]) {
        let _newEntry = new Object();
        let callType = new CallType();

        _newEntry.allCallsArray = new Array();
        _newEntry.name = callLog.name;
        _newEntry.phoneNumber = phoneNumber.phoneNumber;
        _newEntry.duration = 0;
        _newEntry.callType = callType;
        this.history[phoneNumber.phoneNumber] = _newEntry;
      }
      this.history[phoneNumber.phoneNumber].allCallsArray.push(
        new CallLog(
          callLog.id,
          phoneNumber.phoneNumber,
          phoneNumber.prefix,
          callLog.type,
          callLog.rawType,
          callLog.duration,
          callLog.timestamp,
          callLog.dateTime,
        ),
      );
      this.history[phoneNumber.phoneNumber].duration += callLog.duration;
      
      CallType.updateCallType(this.history[phoneNumber.phoneNumber],callLog);
    });

    // removing blocked contacts
    blockedContacts.map(contact => {
      // console.log("deleting contact")

      if(this.history[contact]){
        delete this.history[contact];
      }
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
