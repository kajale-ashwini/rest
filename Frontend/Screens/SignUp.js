import React, { Component } from 'react'
import { SafeAreaView, ScrollView, StyleSheet, TouchableOpacity, View } from 'react-native'
import { Button, Text, TextInput, RadioButton } from 'react-native-paper'
import axios from 'axios'
//import DPicker from './DPicker';
import Opengallery from './Opengallery';
export default class SignUp extends Component {
  constructor(props) {
    super(props);
    this.state = {

      first_name: '',
      last_name: '',
      email: '',
      password: '',
     // dob: '',
      gen: 'first',
      persons:[],
    }
  }


//https://jsonplaceholder.typicode.com/users
 viewdata = () =>{
    axios.get("http://127.0.0.1:80/api/save")
      .then(res => {
        var persons = res.data.items;
        this.setState({ persons });
        //console.log(persons,'get res')
      })
    .catch(error=>{
      console.log(error);
    })
   }

   
  submit = () => {
    console.log(this.state);
    axios.post("http://127.0.0.1:80/api/save",this.state)
      .then(response => {
        console.log(response);
      })
      .catch(error => {
        console.log(error);
      })
  }
  
  render() {
    const { data } = this.state
    const { gen } = this.state
    return (
      <SafeAreaView style={styles.container}>
        <Text style={styles.head}>Sign Up</Text>
        <ScrollView style={{ marginHorizontal: 5 }}>

          <Text>select picture</Text>
          <View style={{ marginTop: 20, width: 100, borderRadius: 150, alignSelf: 'center' }}>
            <Button mode="contained" onPress={() => this.props.navigation.navigate('Opencamera')}>
              camera
            </Button>
          </View>

          <View>
            <Opengallery />
          </View>


          <TextInput style={{ margin: 10, width: 250 }}
            label="First Name"
            value={this.state.first_name}
            onChangeText={first_name => this.setState({ first_name })}
            theme={{
              colors: {
                background: "transparent",
              },
            }}
          />

          <TextInput style={{ margin: 10, width: 250 }}
            label="Last Name"
            value={this.state.last_name}
            onChangeText={last_name => this.setState({ last_name })}
            theme={{
              colors: {
                background: "transparent",
              },
            }}
          />

          <TextInput style={{ margin: 10, width: 250 }}
            label="Email"
            value={this.state.email}
            onChangeText={email => this.setState({ email })}
            theme={{
              colors: {
                background: "transparent",
              },
            }}
          />

          <TextInput style={{ margin: 10, width: 250 }}
            label="Password"
            value={this.state.password}
            onChangeText={password => this.setState({ password })}
            theme={{
              colors: {
                background: "transparent",
              },
            }}
          />

          {/*<View style={{marginTop:10}}>
                  <DPicker/>
                </View>*/}


          <Text>Select gender</Text>
          <View style={{ flexDirection: 'row', marginTop: 5 }}>
            <Text style={styles.txt1}>Male</Text>
            <RadioButton
              value="Male"
              status={gen === 'Male' ? 'checked' : 'unchecked'}
              onPress={() => { this.setState({ gen: 'Male' }); }}
            />
            <Text style={styles.txt1}>Female</Text>
            <RadioButton
              value="Female"
              status={gen === 'Female' ? 'checked' : 'unchecked'}
              onPress={() => { this.setState({ gen: 'Female' }); }} />
          </View>


          <View style={{flexDirection:'row',marginTop: 70, width: 100}}>
            {/*onPress={() =>this.props.navigation.navigate('Hotel')}*/}
            <Button mode="contained" onPress={this.submit}>
              SignUp
            </Button>
            
            <View style={{marginLeft:20}}>
            <Button mode="contained" onPress={this.viewdata}>
              View Data
            </Button>
            </View>
          </View>
            


          <View>
          <ul>       
           {this.state.persons.map(person => 
           <li key={person.id}>
           {person.first_name},
           {person.last_name},
           {person.email},
           {person.password},
           {person.gen}
           </li>)} 
          </ul>
          </View>
             
          
              
          

        </ScrollView>
      </SafeAreaView>
    )
  }
}
const styles = StyleSheet.create({
  container: {
    flex: 1,
    position: "relative",
    margin: 10,
    alignItems: 'center',
    //justifyContent:'center',
    // backgroundColor: "pink",
  },
  head: {
    color: "#7a25fa",
    textAlign: "center",
    height: 40,
    fontSize: 20,
    fontWeight: "bold",
    marginBottom: 20,
    marginTop: 10,
    justifyContent: "center",
  },
  img: {
    width: 200,
    height: 200,
    marginLeft: 50,
    backgroundColor: 'black',
    alignItems: 'center',
    borderRadius: 100
  }

})



/*axios.get('https://randomuser.me/api/')
  .then(function (response) {
    console.log(response.data);
  })
  .catch(function (error) {
    console.log(error);
  });
*/
