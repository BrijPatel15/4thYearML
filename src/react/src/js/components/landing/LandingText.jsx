import React, { Component } from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
class LandingText extends Component {
    constructor(){
        super();
        this.state = {modes: ["Music Mode","Jam Mode","Debug Mode"],};
    }
    render(){
        return(
            <div className="container content-wrapper">
                <div className="landing-text">Welcome!</div>
                <div className="sub-text">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Inventore ipsam similique itaque!</div>
                <div className="pt-4 mx-auto select">
                    <div className="dropdown"> 
                        <button className="btn-xlg border-0 btn-secondary dropdown-toggle modes" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Select Mode
                        </button>
                        <div className="dropdown-menu" aria-labelledby="dropdownMenuButton"> 
                            <div className="dropdown-item" onClick={(e)=>this.setMode('MUSIC')}>{this.state.modes[0]}</div>
                            <div className="dropdown-item" onClick={(e)=>this.setMode('JAM')}>{this.state.modes[1]}</div>
                        <div className="dropdown-divider"></div>
                            <div className="dropdown-item" onClick={(e)=>this.setMode('DEBUG')}>{this.state.modes[2]}</div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
    setMode(newmode){
        this.props.viewHandler(newmode)
    }
}

export default LandingText;