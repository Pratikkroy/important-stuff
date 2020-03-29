import React, {Component} from 'react';
import {View, Text, TouchableOpacity} from 'react-native';
import styles from './styles';
import DateTime from '../../../utils/datetime';
import Details from '../../details/index';

export default class AllCallsComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      key: props.keys,
      duration: DateTime.convertSecondsToMinutes(props.duration),
      callType: props.callType
    };
  }

  renderKey(){
    let text = this.state.key.split("__");
    if(text.length==1){
      return(
        <Text>{this.state.key}</Text>
      );
    } 
    else {
      return (
        <View>
          <Text>{text[0]}</Text>
          <Text>{text[1]}</Text>
        </View>
      )
    }
  }
  
  render() {
    return (
      
        <View style={[styles.container, this.props.style]}>
          <View style={styles.top}>
          </View>
          <View style={styles.mid}>
            <View style={styles.midLeft}>
              {this.renderKey()}
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
    );
  }
}
