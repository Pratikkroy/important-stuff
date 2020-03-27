import React, {Component} from 'react';
import {View, Text, TouchableOpacity} from 'react-native';
import styles from './styles';
import DateTime from '../../../utils/datetime';

export default class CallHistoryComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      durationStr: props.durationStr?props.durationStr:'Total',
      name: props.name,
      phoneNumber: props.phoneNumber,
      duration: DateTime.convertSecondsToMinutes(props.duration),
      callType: props.callType,
      isTouchable: props.isTouchable,
    };
  }

  onSelect(){
    console.log("Pressed....")
    if(this.state.isTouchable){
      console.log("Pressed")
    }
    
  }
  
  render() {
    return (
      <TouchableOpacity
        onPress={() => this.onSelect()}>
        <View style={[styles.container, this.props.style]}>
          <View style={styles.top}>
            <Text style={styles.durationStr}>{this.state.durationStr}</Text>
          </View>
          
          <View style={styles.mid}>
            <View style={styles.midLeft}>
              {this.state.name != null ? (
                <Text>{this.state.name}</Text>
              ) : (
                <View />
              )}
              <Text>{this.state.phoneNumber}</Text>
            </View>
            <View style={styles.midRight}>
              <Text>Duration-{this.state.duration.minutes}m</Text>
              <Text> </Text>
              {this.state.duration.seconds!=0?
                (<Text>
                  {this.state.duration.seconds}s
                </Text>)
                :(<View/>)
              }
            </View>
          </View>
          <View style={styles.bottom}>
            <Text>
              I-{this.state.callType.INCOMING}    
            </Text>
            <Text>
              O-{this.state.callType.OUTGOING}
            </Text>
            <Text>
              M-{this.state.callType.MISSED}
            </Text>
            <Text>
              NA-{this.state.callType.NOT_ANSWERED}
            </Text>
            <Text>
              U-{this.state.callType.UNKNOWN}
            </Text>
          </View>
        </View>
      </TouchableOpacity>  
    );
  }
}
