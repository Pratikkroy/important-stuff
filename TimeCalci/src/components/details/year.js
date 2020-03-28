import React, {Component} from 'react';
import {View, Text} from 'react-native';
import CallHistoryListComponent from '../common/callHistoryListComponent/index'


export default class Year extends Component {
    
    constructor(props) {
        super(props);
    }
    
    render(){
        return(
            <View style={{ flex: 1, backgroundColor: '#652419' }} >
                <Text>Year</Text>
            </View>
        );
    }
}