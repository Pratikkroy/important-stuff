import React, {Component} from 'react';
import {
    SafeAreaView,
    FlatList
} from 'react-native';
import CallHistoryComponent from '../callHistoryComponent/index';

export default class CallHistoryListComponent extends Component {

    state = {isTouchable:false};

    constructor(props) {
      super(props);
      this.state.navigation = props.navigation?props.navigation:null;
      this.state.isTouchable = props.isTouchable? props.isTouchable:false;
    }

    renderCallHistoryComponent(item){
        return (
            <CallHistoryComponent
            name={item.name}
            phoneNumber={item.phoneNumber}
            duration={item.duration}
            callType={item.callType}
            allCallsArray={item.allCallsArray}
            isTouchable={this.state.isTouchable}
            navigation={this.state.navigation}
            />
        );
    }

    render(){
      return (
        <SafeAreaView>
            <FlatList
              // when seraching on homepage everytime this render will be called everytime and 
              // we need to pass filteredCallHistoryArr, but contructor will not be called everytime.
              // So using this.props.filteredCallHistoryArr
              data={this.props.filteredCallHistoryArr}
              renderItem={({ item }) => this.renderCallHistoryComponent(item)}
              extraData={this.state}
              keyExtractor={item => item.phoneNumber}
            />
        </SafeAreaView>
      );
    }
}