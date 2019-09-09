import React, { Component } from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import { LazyLog } from "react-lazylog"
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
                        <button onClick={(e)=> this.startTest()}>Test</button>
                        <label >Motor #</label>
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
                <LazyLog url={'http://127.0.0.1:5000/api/log'} enableSearch follow={true}></LazyLog>
            </div>
        )
    }
    startTest(){
        fetch('http://127.0.0.1:5000/api/test', {method: 'get'})
            .then (res => res.json())
            .then ((data)=> {
                if (data.status_code===200)
                    // this.setState();
                    this.handleErrorShow('Tests are running!');
                else
                    this.handleErrorShow(data.message);
            });
    }
}
export default DebugPage;