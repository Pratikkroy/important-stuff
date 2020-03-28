import React, {Component} from 'react';
import {View, Text} from 'react-native';
import CallHistoryListComponent from '../common/callHistoryListComponent/index'


export default class Month extends Component {
    
    constructor(props) {
        super(props);
    }
    
    render(){
        return(
            <View style={{ flex: 1, backgroundColor: '#002412' }} >
                <Text>Month</Text>
            </View>
        );
    }
}