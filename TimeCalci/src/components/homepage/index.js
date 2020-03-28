/* eslint-disable prettier/prettier */
import React, {Component} from 'react';
import {
  View,
  Text,
  TextInput,
  PermissionsAndroid,
  BackHandler,
  Alert,
} from 'react-native';
import ManageCallLogs from 'react-native-manage-call-logs';
import CallHistory from '../../dataobjects/callHistory';
import CallHistoryListComponent from '../common/callHistoryListComponent/index';
import SearchService from './services';
import styles from './styles';

export default class Homepage extends Component {

  state = {
    isReadCallLogsPermissionGiven: false,
    callHistoryObj: null,
    callHistoryArr: null,
    filteredCallHistoryArr: null,
    searchTextInputValue: ''
  };

  constructor(props) {
    super(props);
    this.state.navigation = props.navigation;
    this.state.isTouchable = props.isTouchable?props.isTouchable:false;
    this.searchService = new SearchService();
  }

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

  onSearchInputTextChange(){

    if(this.state.searchTextInputValue.trim().length==0){
      this.setState({filteredCallHistoryArr:this.state.callHistoryArr})
    } else if(!isNaN(this.state.searchTextInputValue.trim().charAt(0).toString())){
      this.setState(
        {filteredCallHistoryArr:this.searchService.searchByNumber(this.state.callHistoryArr,this.state.searchTextInputValue) }
      );
    }
    else {
      this.setState(
        {filteredCallHistoryArr:this.searchService.searchByName(this.state.callHistoryArr,this.state.searchTextInputValue) }
      );
    }

  }

  createCallHistory(){
    ManageCallLogs.getAll().then(data => {
      let callHistoryObj = new CallHistory(data);
      let callHistoryArr = callHistoryObj.getCallHistoryArray();
      this.setState({
        callHistoryObj: callHistoryObj,
        callHistoryArr: callHistoryArr,
        filteredCallHistoryArr: callHistoryArr
      });
    });
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
    
    return (
      <View style={styles.container}>
        <View style={styles.searchBar}>
        
          <TextInput
            style={styles.searchTextInput}
            onChangeText={(text) => {
              this.state.searchTextInputValue = text;
              this.setState({searchTextInputValue:text});
              this.onSearchInputTextChange(); 
              }
            }
            value={this.state.searchTextInputValue}
          />
        
        </View>
        <View style={styles.searchResults}>
          {this.state.callHistoryObj != null ? (
            <CallHistoryListComponent
              navigation={this.state.navigation}
              filteredCallHistoryArr={this.state.filteredCallHistoryArr}
              isTouchable={true}
            />
            
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


