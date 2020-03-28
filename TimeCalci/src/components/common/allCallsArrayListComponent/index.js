/* eslint-disable prettier/prettier */
import React, {Component} from 'react';
import {
  View,
  Text,
  SafeAreaView,
  FlatList,
  BackHandler,
  Alert,
} from 'react-native';
import AllCallsComponent from '../allCallsComponent/index';
import styles from './styles';

export default class AllCallsArrayListComponent extends Component {

  state = {

  };

  constructor(props) {
    super(props);
    this.state.name = props.name;
    this.state.phoneNumber = props.phoneNumber;
    this.state.allCallsArray = props.allCallsArray;
  }

  // lifecycle methods
  async componentDidMount(){
    
  }

  renderAllCallsArray(item){
    return (
        <AllCallsComponent
          keys={item.key}
          duration={item.duration}
          callType={item.callType}
        />  
      );
  }

  render() {
    return (
      <View style={styles.container}>
        <View style={styles.nameNumberBar}>
        
          {this.state.name != null ? (
            <Text>{this.state.name}</Text>
          ) : (
            <View />
          )}
          <Text>{this.state.phoneNumber}</Text>
        
        </View>
        <View style={styles.allCallsArrayListBar}>
          <SafeAreaView>
            <FlatList
              data={this.props.allCallsArray}
              renderItem={({ item }) => this.renderAllCallsArray(item)}
              extraData={this.state}
              keyExtractor={item => item.key}
            />
          </SafeAreaView>
        </View>
      </View>
    );
  }
}


