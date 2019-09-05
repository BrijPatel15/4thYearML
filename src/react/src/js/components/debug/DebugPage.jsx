import React, { Component } from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
class DebugPage extends Component {
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
                <div className="landing-text">Debug Mode!</div>
                <div className="sub-text">PRIVATE: dont touch if you dont know what you are doing! Debug and calibrate the assistant.</div>
                <div className="mx-auto select">
                    <div className="form-group">
                        <label for="exampleFormControlSelect1">Motor #</label>
                        <select className="form-control" id="exampleFormControlSelect1">
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>
                        <option>5</option>
                        <option>6</option>
                        </select>
                        <input placeholder="steps"></input>
                    </div>
                </div>
            </div>
        )
    }
}
export default DebugPage;