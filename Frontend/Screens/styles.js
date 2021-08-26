import { StyleSheet, Picker } from "react-native";
import { TextInput, Button } from "react-native-paper";
export default StyleSheet.create({
    container: {
        flex: 1,
        position: "relative",
        margin: 10,
        alignItems:'center',
        justifyContent:'center',
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
      txt1:{
        fontSize:20,
        position:'relative',
        top:20,
        alignItems:'center',
        marginLeft:60
      },
      txt2:{
        marginTop:30, 
        fontSize:15,
        margin:10
      },
      img:{
        width: 200, 
        height: 200, 
        marginLeft:50,
        backgroundColor:'black', 
        alignItems:'center', 
        borderRadius:100
      }
})