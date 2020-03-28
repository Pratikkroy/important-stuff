import React, {Component} from 'react';
import {View, Text} from 'react-native';
import CallHistoryListComponent from '../common/callHistoryListComponent/index'


export default class Week extends Component {
    
    constructor(props) {
        super(props);
    }
    
    render(){
        return(
            <View style={{ flex: 1, backgroundColor: '#102091' }} >
                <Text>Week</Text>
            </View>
        );
    }
}