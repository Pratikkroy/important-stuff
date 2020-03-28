import {StyleSheet} from 'react-native';
import {wp, hp} from '../../utils/percentagesToDP';
import {COLORS} from '../../constants/colors';

const searchBarHeight = 20;
const searchResultsHeight = 100 - searchBarHeight - 5;

const styles = StyleSheet.create({
  container: {
    height: hp(100),
    width: wp(100),
    flexDirection: 'column',
  },
  searchBar: {
    height: hp(searchBarHeight),
    width: wp(100),
    justifyContent: 'center',
    alignItems: 'center',
    borderBottomWidth: 2,
    borderColor: COLORS.BLACK,
  },
  searchResults: {
    height: hp(searchResultsHeight),
    width: wp(100),
  },
  callHistoryComponent: {
  },
  searchTextInput: {
    height: hp(5), 
    width: wp(60),
    
    
    borderColor: COLORS.GRAY, 
    borderWidth: 1
  },
});

export default styles;
