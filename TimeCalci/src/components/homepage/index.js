/* eslint-disable prettier/prettier */
import React, {Component} from 'react';
import {
  SafeAreaView,
  FlatList,
  View,
  Text,
  PermissionsAndroid,
  BackHandler,
  Alert,
} from 'react-native';
import ManageCallLogs from 'react-native-manage-call-logs';
import CallHistory from '../../dataobjects/callHistory';
import CallHistoryComponent from '../common/callHistoryComponent/index';

import styles from './styles';

export default class HomePage extends Component {

  state = {
    isReadCallLogsPermissionGiven: false,
    callHistoryObj: null,
    callHistoryArr: null
  };

  // class helper methods
  async askReadCallLogsPermission(){
    try {
      await PermissionsAndroid.requestMultiple([
              PermissionsAndroid.PERMISSIONS.READ_CALL_LOG,
          ]).then(result => {
              if (result['android.permission.READ_CALL_LOG'] === 'granted'){
                console.log('ReadCallLogsPermission granted');
                this.state.isReadCallLogsPermissionGiven = true;
              }
              else {
                console.log('ReadCallLogsPermission not given');
                this.state.isReadCallLogsPermissionGiven = false;
              }
          });
      }
      catch (ex) {
        console.log(ex);
        this.state.isReadCallLogsPermissionGiven = false;
      }
      return this.state.isReadCallLogsPermissionGiven;
  }

  exitApp(){
    BackHandler.exitApp();
  }

  createCallHistory(){
    ManageCallLogs.getAll().then(data => {
      console.log(data);
      let callHistoryObj = new CallHistory(data);
      this.setState({
        callHistoryObj: callHistoryObj,
        callHistoryArr: callHistoryObj.getCallHistoryArray(),
      });
    });
  }

  renderCallHistoryComponent(name, phoneNumber, duration){
    return (
      <CallHistoryComponent
        name={name}
        phoneNumber={phoneNumber}
        duration={duration}
        style={styles.callHistoryComponent}
      />
    );
  }

  // lifecycle methods
  async componentDidMount(){
    this.askReadCallLogsPermission().then(
      result => {
        if (!result){
          Alert.alert(
            'Permissions',
            'Read call logs permission is not given',
            [
              {text: 'OK', onPress: () => this.exitApp()},
            ],
            { cancelable: false }
          );
        }
      }
    );
    this.createCallHistory();
  }

  render() {
    console.log("render",this.state.callHistoryObj);
    return (
      <View style={styles.container}>
        <View style={styles.searchBar}>
          <Text>Hello World search bar</Text>
        </View>
        <View style={styles.searchResults}>
          {this.state.callHistoryObj != null ? (
            <SafeAreaView>
              <FlatList
                data={this.state.callHistoryArr}
                renderItem={({ item }) => this.renderCallHistoryComponent(item.name, item.phoneNumber, item.duration)}
                extraData={this.state}
                keyExtractor={item => item.phoneNumber}
              />
            </SafeAreaView>
          ):(
            <View>
              <Text/>
            </View>
          )}
        </View>
      </View>
    );
  }
}


