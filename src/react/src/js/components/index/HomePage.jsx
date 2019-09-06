import React, { Component } from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import  LandingText  from "../landing/LandingText.jsx";
import PlayMusicPage from "../music/PlayMusicPage.jsx";
import DebugPage from "../debug/DebugPage.jsx";
class HomePage extends Component {
    constructor(){
        super();

        this.state = {
            title: "Electronic Jam Assitant",
            modes: ["Music","Jam","Debug"],
            currMode: 'DEFAULT'
            
        }
        this.viewHandler=this.viewHandler.bind(this);

    }
    viewHandler(currMode){
        this.setState({currMode:currMode})
    }
    componentDidMount(){
        fetch('http://127.0.0.1:5000/api/mode', {method: 'get'})
        .then (res => res.json())
        .then ((data)=> {
            this.setState({currMode: data});
            console.log(this.state.currMode);
        });
    }
    render(){
        return(
            <Router>
                <div className="wrapper">
                    
                    <div className="navbar navbar-expand-lg navbar-light bg-light">
                        <div className="navbar-brand" onClick={(e) => this.setMode('DEFAULT')}>{this.state.title}</div>
                        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                            <span className="navbar-toggler-icon"></span>
                        </button>
                        <div className="collapse navbar-collapse" id="navbarSupportedContent">
                            <ul className="navbar-nav mr-auto">
                                <li  className="nav-item pr-3" onClick={(e) => this.setMode('MUSIC')}>{this.state.modes[0]}</li>
                                <li  className="nav-item pr-3" onClick={(e) => this.setMode('JAM')}>{this.state.modes[1]}</li>
                                <div className="nav-divider"></div>
                                <li className="nav-item pr-3" onClick={(e) => this.setMode('DEBUG')}>{this.state.modes[2]}</li>
                            </ul>
                        </div>
                    </div>
                    {this.showModeView()}
                </div>
            </Router>
        )
    }

    showModeView(){
        if (this.state.currMode==='DEFAULT'){
            return <LandingText viewHandler={this.viewHandler}/>;
        }
        else if (this.state.currMode==='MUSIC'){
            return <PlayMusicPage/>;
        }
        else if (this.state.currMode==='DEBUG'){
            return <DebugPage/>;
        }else if (this.state.currMode==='JAM'){
            return <div>JAM MODE</div>;
        }
    }
    setMode(newmode){
        // console.log(newmode);
        fetch('http://127.0.0.1:5000/api/mode', {method: 'post', header: {'Accept': 'application/json', 'Content-Type': 'application/json'},body: JSON.stringify({ data: newmode})})
        .then (res => res.json())
        .then ((data)=> {
            
            this.setState({currMode: data.data});
            console.log(this.state.currMode);
        });
    }
}
export default HomePage;
