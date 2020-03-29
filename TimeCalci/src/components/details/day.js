import React, {Component} from 'react';
import {View, Text} from 'react-native';
import AllCallsArrayListComponent from '../common/allCallsArrayListComponent/index';
import DateTimefrom from '../../utils/datetime';
import CallGrouping from '../../dataobjects/callGrouping'
import {CALL_GROUPING_TYPE} from '../../constants/callGroupingType';
import CallType from '../../dataobjects/callType';

export default class Day extends Component {
    
    state = {};
    constructor(props) {
        super(props);
        this.state.name = props.name;
        this.state.phoneNumber = props.phoneNumber;
        this.state.dayWiseAllCallsArray = this.getDayWiseAllCallsArray(props.allCallsArray);
    }

    getDayWiseAllCallsArray(allCallsArray){
        let dayWiseAllCallsObj = {};
        allCallsArray.forEach(element => {
            let key = element.dateTime.split(" ")[0];
            if(!dayWiseAllCallsObj[key]){
                dayWiseAllCallsObj[key] = new CallGrouping({
                    groupingType: CALL_GROUPING_TYPE.DAY,
                    key: key
                });
            }
            dayWiseAllCallsObj[key].duration += element.duration;

            CallType.updateCallType(dayWiseAllCallsObj[key],element);
        })
        return this.convertObjToArray(dayWiseAllCallsObj);
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
                allCallsArray = {this.state.dayWiseAllCallsArray}
            />
            
        );
    }
}