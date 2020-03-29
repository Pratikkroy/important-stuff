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
        this.state.monthWiseAllCallsArray = this.getMonthWiseAllCallsArray(props.allCallsArray);
    }

    getMonthWiseAllCallsArray(allCallsArray){        
        let monthWiseAllCallsObj = {};
        allCallsArray.forEach(element => {
            let monthYear = element.dateTime.split(" ")[0].split("-");
            let key = monthYear[1]+' '+monthYear[2];
            if(!monthWiseAllCallsObj[key]){
                monthWiseAllCallsObj[key] = new CallGrouping({
                    groupingType: CALL_GROUPING_TYPE.MONTH,
                    key: key
                });
            }
            monthWiseAllCallsObj[key].duration += element.duration;

            CallType.updateCallType(monthWiseAllCallsObj[key],element);
        })
        return this.convertObjToArray(monthWiseAllCallsObj);
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
                allCallsArray = {this.state.monthWiseAllCallsArray}
            />
            
        );
    }
}