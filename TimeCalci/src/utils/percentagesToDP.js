import {
  widthPercentageToDP as wp,
  heightPercentageToDP as hp,
} from 'react-native-responsive-screen';

function heightPercentageToDP(percentage) {
  if (isNaN(percentage)) {
    throw 'Not a valid number';
  }
  return hp(percentage.toString() + '%');
}

function widthPercentageToDP(percentage) {
  if (isNaN(percentage)) {
    throw 'Not a valid number';
  }
  return wp(percentage.toString() + '%');
}

// export default to used where only a single object has to be returned
// export default {
//   widthPercentageToDP,
//   heightPercentageToDP,
// };

export {widthPercentageToDP as wp, heightPercentageToDP as hp};
