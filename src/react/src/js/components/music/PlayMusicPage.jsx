import React, { Component } from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
class LandingText extends Component {
    constructor(){
        super();
        this.state = {
            modes: ["Music Mode","Jam Mode","Debug Mode"],
            isPlaying: false
            };
    }
    render(){
        return(
            <div className="container content-wrapper">
                <div className="landing-text">Play Mode!</div>
                <div className="sub-text">Let the assitant play a song for you!</div>
                <div className="mx-auto select">
                   <div className="card">
                   <img src="https://www.cmuse.org/wp-content/uploads/2017/03/guitar_hurdles.jpg" className="card-img-top" alt="..."/>
                       <div className="card-body">
                           <button onClick={this.toggleMusic()}>{this.btnLabel()}</button>
                       </div>
                   </div>
                </div>
            </div>
        )
    }
    toggleMusic(){
        if (this.state.isPlaying){
            fetch('http://127.0.0.1:5000/api/pause', {method: 'get'})
            .then (res => res.json())
            .then ((data)=> {
                this.setState({isPlaying: true});
                // this.setState({currMode: data.data});
                console.log(this.state.currMode);
            });
        }else{
            fetch('http://127.0.0.1:5000/api/play', {method: 'get'})
            .then (res => res.json())
            .then ((data)=> {
                this.setState({isPlaying: false});
                // this.setState({currMode: data.data});
                console.log(this.state.currMode);
            });
        }
    }
    btnLabel(){
        if (this.state.isPlaying){
            return "Pause";
        }else{
            return "Play";
        }
    }
}
export default LandingText;