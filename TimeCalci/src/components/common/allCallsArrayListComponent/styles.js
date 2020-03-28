import {StyleSheet} from 'react-native';
import {wp, hp} from '../../../utils/percentagesToDP';
import {COLORS} from '../../../constants/colors';

const styles = StyleSheet.create({
  container: {
    width: wp(100),
    flexDirection: 'column',
  },
  nameNumberBar: {
    height: hp(20),
    width: wp(100),
    justifyContent: 'center',
    alignItems: 'center',
    borderBottomWidth: 2,
    borderColor: COLORS.BLACK,
  },
  allCallsArrayListBar: {
    height: hp(70),
    width: wp(100),
    backgroundColor: COLORS.DEFAULT_BACKGROUND_COLOR,
  },
  top: {
    height: hp(0),
    paddingHorizontal: wp(5),
    justifyContent: 'flex-end',
  },
  mid: {
    height: hp(6),
    paddingHorizontal: wp(5),
    flexDirection: 'row',
  },
  midLeft: {
    height: hp(6),
    width: wp(45),
    justifyContent: 'center',
  },
  midRight: {
    height: hp(6),
    width: wp(45),
    flexDirection: 'row',
    alignItems: 'center',
  },
  bottom: {
    height: hp(4),
    width: '100%',
    flexDirection: 'row',
    justifyContent: 'space-evenly',
    alignItems: 'center',
    backgroundColor: COLORS.LIGHT_GRAY,
  },
});

export default styles;
