import React, { Component } from 'react'
import { Text, View } from 'react-native'
import {Button} from 'react-native-paper';
import axios from 'axios';
export default class Fetch extends Component {
          constructor(){
              super();
              this.state={
                abc : []
              }
          }
    submit=()=>{ 
       axios.get("https://jsonplaceholder.typicode.com/todos")
        .then(response =>{   
            const abc = response.data;
            this.setState({abc})
                //console.log(response);
        })
        .catch(error=>{
          console.log(error);
        })
       }
      
      
    render() {
        const { data } = this.state
        return (
            <View>
              <Button style={{width:140, alignSelf:"center"}}
              icon="camera" mode="contained"  onPress={this.submit}>
               Pull data
            </Button>
              <View>
              {this.state.abc.slice(0, 20).map(abc => 
              <li>
                <View style={{margin:2,width:250,borderRadius:10, backgroundColor:'pink'}}>{abc.title}
                </View>
            </li>
            )}
              </View>
              
               
            </View>
        )
    }
}
