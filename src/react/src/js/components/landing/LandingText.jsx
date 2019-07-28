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
                        {/* <a className="dropdown-item" href="#">{this.state.modes[0]}</a> */}
                        <Link to="/music" className="dropdown-item">{this.state.modes[0]}</Link>
                        {/* <a className="dropdown-item" href="#">{this.state.modes[1]}</a> */}
                        <Link to="/jam" className="dropdown-item">{this.state.modes[1]}</Link>
                        <div className="dropdown-divider"></div>
                        {/* <a className="dropdown-item" href="#">{this.state.modes[2]}</a> */}
                        <Link to="/debug" className="dropdown-item">{this.state.modes[2]}</Link>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}
export default LandingText;