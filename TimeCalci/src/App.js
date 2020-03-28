/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */
import 'react-native-gesture-handler';
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { View, StatusBar} from 'react-native';
import Homepage from './components/homepage/index.js';
import Details from './components/details/index';

const Stack = createStackNavigator();


const App: () => React$Node = () => {
  console.reportErrorsAsExceptions = false;
  
  return (
    // <NavigationContainer>
    //   <StatusBar barStyle="dark-content" />
    //   <Homepage/>
    // </NavigationContainer>
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Homepage">
        <Stack.Screen name="Homepage" component={Homepage} options={{ title: 'Home' }}/>
        <Stack.Screen name="Details" component={Details} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;

