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
        this.state.yearWiseAllCallsArray = this.getYearWiseAllCallsArray(props.allCallsArray);
    }

    getYearWiseAllCallsArray(allCallsArray){        
        let yearWiseAllCallsObj = {};
        allCallsArray.forEach(element => {
            let key = element.dateTime.split(" ")[0].split("-")[2];
            if(!yearWiseAllCallsObj[key]){
                yearWiseAllCallsObj[key] = new CallGrouping({
                    groupingType: CALL_GROUPING_TYPE.YEAR,
                    key: key
                });
            }
            yearWiseAllCallsObj[key].duration += element.duration;

            CallType.updateCallType(yearWiseAllCallsObj[key],element);
        })
        return this.convertObjToArray(yearWiseAllCallsObj);
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
                allCallsArray = {this.state.yearWiseAllCallsArray}
            />
            
        );
    }
}