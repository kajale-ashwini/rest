import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
//import Calling from './Screens/Nav/Calling';
import SignUp from './Screens/SignUp';
//import Swiperimplement from './Screens/Swiperimplement';

//import Toptab from './AssignFirst/Toptab';

export default function App() {
  return (
  /* <NavigationContainer>
      <Calling/>
   </NavigationContainer>*/
  // <Toptab/>
  <SignUp/>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
