import {StyleSheet} from 'react-native';
import {wp, hp} from '../../../utils/percentagesToDP';
import {COLORS} from '../../../constants/colors';

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    backgroundColor: COLORS.DEFAULT_BACKGROUND_COLOR,
    height: hp(10),
    width: wp(100),
    paddingHorizontal: wp(5),
    paddingVertical: hp(1),
    borderLeftWidth: 5,
    borderBottomWidth: 5,
    borderColor: COLORS.GRAY,
  },
  left: {
    flex: 1,
    height: hp(100),
    width: wp(50),
    flexDirection: 'row',
    justifyContent: 'flex-start',
  },
  right: {
    flex: 1,
    height: hp(100),
    width: wp(100),
    flexDirection: 'row-reverse',
    justifyContent: 'flex-start',
  },
  nameNumberContainer: {
  },
  durationAndTypeContainer: {

  },
});

export default styles;
