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
    };
  }

  render() {
    return (
      <View style={[styles.container, this.props.style]}>
        <View style={styles.left}>
          <View>
            {this.state.name != null ? (
              <Text>{this.state.name}</Text>
            ) : (
              <Text />
            )}
            <Text>{this.state.phoneNumber}</Text>
          </View>
        </View>
        <View style={styles.right}>
          <Text>Duration-{this.state.duration}</Text>
        </View>
      </View>
    );
  }
}
