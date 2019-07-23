import React, { Component } from "react";
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import Dropzone from 'react-dropzone'
class LandingText extends Component {
    constructor(){
        super();
        this.state = {
            modes: ["Music Mode","Jam Mode","Debug Mode"],
            isPlaying: "Play",
            nowPlaying: ""
            };
    }
    render(){
        return(
            <div className="container content-wrapper">
                <div className="landing-text">Play Mode!</div>
                <div className="sub-text">Let the assitant play a song for you!</div>
                <div className="mx-auto musicplayer">
                   <div className="card">
                   <img src="https://www.cmuse.org/wp-content/uploads/2017/03/guitar_hurdles.jpg" className="card-img-top" alt="..."/>
                       <div className="card-body">
                            <input className="fileupload" ref={input => this.fileUploadRef =input} type="file" name="file" onChange={(event) => this.onChangeHandler(event)}/>
                            {/* <button onClick={(e) => this.toggleMusic(e)}>{this.state.isPlaying}</button> <span>{this.state.nowPlaying}</span> */}
                            <div className="mx-auto musicplayer">
                                <div className="btn-group">
                                    <button type="button" className="btn btn-secondary" onClick={() => this.fileUploadRef.click()}>Upload</button>
                                    <button type="button" className="btn btn-secondary" onClick={() => this.playMusic()}>Play</button>
                                    <button type="button" className="btn btn-secondary" onClick={() => this.stopMusic()}>Stop</button>
                                </div>
                            </div>
                       </div>
                   </div>
                  
                </div>
            </div>
        )
    }
    playMusic(){
        fetch('http://127.0.0.1:5000/api/play', {method: 'get'})
        .then (res => res.json())
        .then ((data)=> {
            this.setState({isPlaying: 'Pause'});
            // this.setState({currMode: data.data});
            // console.log(this.state.currMode);
        });
    }
    stopMusic(){
        fetch('http://127.0.0.1:5000/api/pause', {method: 'get'})
            .then (res => res.json())
            .then ((data)=> {
                this.setState({isPlaying: 'Play', nowPlaying:data.data});
                // this.setState({currMode: data.data});
                // console.log(this.state.currMode);
            });
    }
    onChangeHandler(event){
        console.log(event.target.files[0])
        const data = new FormData() 
        data.append('file', event.target.files[0])
        fetch('http://127.0.0.1:5000/api/upload', {method: 'post',body:data })
        .then (res => res.json())
        .then ((data)=> {
            
            // this.setState({currMode: data.data});
            console.log(data);
        });
    }
    upload(){
        this.refs.fileupload.click();
    }
}
export default LandingText;