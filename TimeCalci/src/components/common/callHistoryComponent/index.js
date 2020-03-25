import React, {Component} from 'react';
import {View, Text} from 'react-native';
import styles from './styles';

export default class CallHistoryComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      name: props.name,
      phoneNumber: props.phoneNumber,
      duration: props.duration,
      callType: props.callType,
    };
  }

  render() {
    return (
      <View style={[styles.container, this.props.style]}>
        <View style={styles.left}>
          <View style={styles.nameNumberContainer}>
            {this.state.name != null ? (
              <Text>{this.state.name}</Text>
            ) : (
              <Text />
            )}
            <Text>{this.state.phoneNumber}</Text>
          </View>
        </View>
        <View style={styles.right}>
          <View style={styles.durationAndTypeContainer}>
            <Text>Duration-{this.state.duration}</Text>
            <Text>
              I-{this.state.callType.INCOMING}    O-{this.state.callType.OUTGOING} 
            </Text>
            <Text>
              M-{this.state.callType.MISSED}      NA-{this.state.callType.NOT_ANSWERED}
            </Text>
            <Text>
              U-{this.state.callType.UNKNOWN}
            </Text>
          </View>
        </View>
      </View>
    );
  }
}
