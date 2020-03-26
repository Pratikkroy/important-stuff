import {StyleSheet} from 'react-native';
import {wp, hp} from '../../../utils/percentagesToDP';
import {COLORS} from '../../../constants/colors';

const styles = StyleSheet.create({
  container: {
    height: hp(13),
    borderWidth: 0,
    borderColor: COLORS.GRAY,
    margin:10,
    backgroundColor: COLORS.DEFAULT_BACKGROUND_COLOR,
  },
  top: {
    height: hp(3),
    paddingHorizontal: wp(5),
    justifyContent: 'flex-end',

  },
  durationStr: {
    fontWeight: 'bold'
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
  nameNumberContainer: {
  },
  durationContainer: {

  },
});

export default styles;
