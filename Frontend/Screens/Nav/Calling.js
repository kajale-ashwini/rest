import React from 'react'
import { createStackNavigator } from '@react-navigation/stack';
import Onboarding from '../Onboarding';
import Chat from '../Chat';
import Perfect from '../Perfect';
//import Swiperimplement from '../Swiperimplement';
import SignUp from '../SignUp';
import Hotel from '../Hotel';
import OpenCamera from '../Opencamera';

const Stack = createStackNavigator();
const Calling = () =>{
    return (
        <Stack.Navigator>
          {/*<Stack.Screen name="Swiperimplement" component={Swiperimplement}/>*/}
          <Stack.Screen name="Onboarding" component={Onboarding} />
          <Stack.Screen name="Chat" component={Chat} />
          <Stack.Screen name="Perfect" component={Perfect} />
        <Stack.Screen name="SignUp" component={SignUp} />
        <Stack.Screen name="Opencamera" component={OpenCamera} />
        <Stack.Screen name="Hotel" component={Hotel} />
      </Stack.Navigator>
        
    )
}

export default Calling;