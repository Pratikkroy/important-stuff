import React, {Component} from 'react';
import {View, Text} from 'react-native';
import AllCallsArrayListComponent from '../common/allCallsArrayListComponent/index';
import DateTime from '../../utils/datetime';
import CallGrouping from '../../dataobjects/callGrouping'
import {CALL_GROUPING_TYPE} from '../../constants/callGroupingType';
import CallType from '../../dataobjects/callType';


export default class Week extends Component {
    
    state = {};
    constructor(props) {
        super(props);
        this.state.name = props.name;
        this.state.phoneNumber = props.phoneNumber;
        this.state.weekWiseAllCallsArray = this.getWeekWiseAllCallsArray(props.allCallsArray);
    }

    getWeekWiseAllCallsArray(allCallsArray){        
        let weekWiseAllCallsObj = {};
        allCallsArray.forEach(element => {
            let key = this.getKey(parseInt(element.timestamp));
            if(!weekWiseAllCallsObj[key]){
                weekWiseAllCallsObj[key] = new CallGrouping({
                    groupingType: CALL_GROUPING_TYPE.WEEK,
                    key: key
                });
            }
            weekWiseAllCallsObj[key].duration += element.duration;

            CallType.updateCallType(weekWiseAllCallsObj[key],element);
        })
        return this.convertObjToArray(weekWiseAllCallsObj);
    }

    getKey(timestamp){
        let lastSundayDate = DateTime.getLastSunday(new Date(timestamp));
        let key = DateTime.convertDateObjToDate(lastSundayDate)+"__";
        lastSundayDate.setDate(lastSundayDate.getDate()+6);
        key += DateTime.convertDateObjToDate(lastSundayDate)
        return key;
    }

    convertObjToArray(obj){
        let arr = new Array();
        for (let [key, value] of Object.entries(obj)) {
            arr.push(value);
          }
          return arr;
    }
    
    render(){
        return(
            <AllCallsArrayListComponent
                name={this.state.name}
                phoneNumber={this.state.phoneNumber}
                allCallsArray = {this.state.weekWiseAllCallsArray}
            />
            
        );
    }
}