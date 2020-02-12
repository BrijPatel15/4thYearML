import React, { Component } from "react";
import ReactDOM from 'react-dom';
import {Modal, Button} from "react-bootstrap";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import Dropzone from 'react-dropzone'
class PlayMusicPage extends Component {
    constructor(){
        super();
        this.state = {
            modes: ["Music Mode","Jam Mode","Debug Mode"],
            isPlaying: "Play",
            nowPlaying: "",
            showError:false,
            errorMessage:'',
            songProcessID: -1000
            };
    }
    render(){
        const handleErrorClose = () => {
            this.setState({showError:false})
        }
        return(
            <div className="container content-wrapper">
                <div className="landing-text">Jam Mode!</div>
                <div className="sub-text">Let the assitant play a with you!</div>
                <div className="mx-auto musicplayer">
                   <div className="card">
                        <input type="text"> </input>
                        <input type="text"> </input>
                        <input type="text"> </input>
                   </div>
                  
                </div>
            </div>
        )
    }
}
export default PlayMusicPage;