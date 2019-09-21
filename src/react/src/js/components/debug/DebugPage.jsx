import React, { Component } from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import { LazyLog } from "react-lazylog"
class DebugPage extends Component {
    constructor(){
        super();
        this.state = {
            modes: ["Music Mode","Jam Mode","Debug Mode"],
            isPlaying: false,
            notesToSend: [
                {
                    note: "",
                    stringId: "string1"
                },
                {
                    note: "",
                    stringId: "string2"
                },
                {
                    note: "",
                    stringId: "string3"
                },
                {
                    note: "",
                    stringId: "string4"
                },
                {
                    note: "",
                    stringId: "string5"
                },
                {
                    note: "",
                    stringId: "string6"
                }
            ]
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
                <div classname="d-flex flex-row" style={{height: '500px'}}>
                    <LazyLog url={'http://127.0.0.1:5000/api/log'} enableSearch follow={true} stream={true}></LazyLog>
                </div>
                <div classname="sub-text">
                    Select the note you want to play.
                </div>
                <div classname="mx-auto">
                    <div classname="fretRow" id="string1">
                        <label>String 1</label>
                        <button class="btn" onClick={() => this.addNote('E1', 'string1')}>E</button>
                        <button class="btn" onClick={() => this.addNote('F1', 'string1')}>F</button>
                        <button class="btn" onClick={() => this.addNote('F#1', 'string1')}>F#</button>
                        <button class="btn" onClick={() => this.addNote('G1', 'string1')}>G</button>
                        <button class="btn" onClick={() => this.addNote('G#1', 'string1')}>G#</button>
                        <button class="btn" onClick={() => this.addNote('A1', 'string1')}>A</button>
                        <button class="btn" onClick={() => this.addNote('A#1', 'string1')}>A#</button>
                        <button class="btn" onClick={() => this.addNote('B1', 'string1')}>B</button>
                        <button class="btn" onClick={() => this.addNote('C1', 'string1')}>C</button>
                        <button class="btn" onClick={() => this.addNote('C#1', 'string1')}>C#</button>
                        <button class="btn" onClick={() => this.addNote('D1', 'string1')}>D</button>
                        <button class="btn" onClick={() => this.addNote('D#1', 'string1')}>D#</button>
                        <button class="btn" onClick={() => this.addNote('E2', 'string1')}>E</button>
                    </div>
                    <div classname="fretRow" id="string2">
                        <label>String 2</label>
                        <button class="btn" onClick={() => this.addNote('B2', 'string2')}>B</button>
                        <button class="btn" onClick={() => this.addNote('C2', 'string2')}>C</button>
                        <button class="btn" onClick={() => this.addNote('C#2', 'string2')}>C#</button>
                        <button class="btn" onClick={() => this.addNote('D2', 'string2')}>D</button>
                        <button class="btn" onClick={() => this.addNote('D#2', 'string2')}>D#</button>
                        <button class="btn" onClick={() => this.addNote('E3', 'string2')}>E</button>
                        <button class="btn" onClick={() => this.addNote('F2', 'string2')}>F</button>
                        <button class="btn" onClick={() => this.addNote('F#2', 'string2')}>F#</button>
                        <button class="btn" onClick={() => this.addNote('G2', 'string2')}>G</button>
                        <button class="btn" onClick={() => this.addNote('G#2', 'string2')}>G#</button>
                        <button class="btn" onClick={() => this.addNote('A2', 'string2')}>A</button>
                        <button class="btn" onClick={() => this.addNote('A#2', 'string2')}>A#</button>
                        <button class="btn" onClick={() => this.addNote('B3', 'string2')}>B</button>
                    </div>
                    <div classname="fretRow" id="string3">
                        <label>String 3</label>
                        <button class="btn" onClick={() => this.addNote('G3', 'string3')}>G</button>
                        <button class="btn" onClick={() => this.addNote('C#3', 'string3')}>C#</button>
                        <button class="btn" onClick={() => this.addNote('A3', 'string3')}>A</button>
                        <button class="btn" onClick={() => this.addNote('A#3', 'string3')}>A#</button>
                        <button class="btn" onClick={() => this.addNote('B4', 'string3')}>B</button>
                        <button class="btn" onClick={() => this.addNote('C3', 'string3')}>C</button>
                        <button class="btn" onClick={() => this.addNote('C#3', 'string3')}>C#</button>
                        <button class="btn" onClick={() => this.addNote('D3', 'string3')}>D</button>
                        <button class="btn" onClick={() => this.addNote('D#3', 'string3')}>D#</button>
                        <button class="btn" onClick={() => this.addNote('E4', 'string3')}>E</button>
                        <button class="btn" onClick={() => this.addNote('F3', 'string3')}>F</button>
                        <button class="btn" onClick={() => this.addNote('F#3', 'string3')}>F#</button>
                        <button class="btn" onClick={() => this.addNote('G-1', 'string3')}>G</button>
                    </div>

                    <div classname="fretRow" id="string4">
                        <label>String 4</label>
                        <button class="btn" onClick={() => this.addNote('D4', 'string4')}>D</button>
                        <button class="btn" onClick={() => this.addNote('D#4', 'string4')}>D#</button>
                        <button class="btn" onClick={() => this.addNote('E5', 'string4')}>E</button>
                        <button class="btn" onClick={() => this.addNote('F-1', 'string4')}>F</button>
                        <button class="btn" onClick={() => this.addNote('F#4', 'string4')}>F#</button>
                        <button class="btn" onClick={() => this.addNote('G-2', 'string4')}>G</button>
                        <button class="btn" onClick={() => this.addNote('G#4', 'string4')}>G#</button>
                        <button class="btn" onClick={() => this.addNote('A-1', 'string4')}>A</button>
                        <button class="btn" onClick={() => this.addNote('A#4', 'string4')}>A#</button>
                        <button class="btn" onClick={() => this.addNote('B-1', 'string4')}>B</button>
                        <button class="btn" onClick={() => this.addNote('C4', 'string4')}>C</button>
                        <button class="btn" onClick={() => this.addNote('C#4', 'string4')}>C#</button>
                        <button class="btn" onClick={() => this.addNote('D5', 'string4')}>D</button>
                    </div>

                    <div classname="fretRow" id="string5">
                        <label>String 5</label>
                        <button class="btn" onClick={() => this.addNote('A5', 'string5')}>A</button>
                        <button class="btn" onClick={() => this.addNote('A#5', 'string5')}>A#</button>
                        <button class="btn" onClick={() => this.addNote('B6', 'string5')}>B</button>
                        <button class="btn" onClick={() => this.addNote('C5', 'string5')}>C</button>
                        <button class="btn" onClick={() => this.addNote('C#5', 'string5')}>C#</button>
                        <button class="btn" onClick={() => this.addNote('D6', 'string5')}>D</button>
                        <button class="btn" onClick={() => this.addNote('D#5', 'string5')}>D#</button>
                        <button class="btn" onClick={() => this.addNote('E6', 'string5')}>E</button>
                        <button class="btn" onClick={() => this.addNote('F5', 'string5')}>F</button>
                        <button class="btn" onClick={() => this.addNote('F#5', 'string5')}>F#</button>
                        <button class="btn" onClick={() => this.addNote('G6', 'string5')}>G</button>
                        <button class="btn" onClick={() => this.addNote('G#5', 'string5')}>G#</button>
                        <button class="btn" onClick={() => this.addNote('A-2', 'string5')}>A</button>
                    </div>

                    <div classname="fretRow" id="string6">
                        <label>String 6</label>
                        <button class="btn" onClick={() => this.addNote('E7', 'string6')}>E</button>
                        <button class="btn" onClick={() => this.addNote('F6', 'string6')}>F</button>
                        <button class="btn" onClick={() => this.addNote('F#6', 'string6')}>F#</button>
                        <button class="btn" onClick={() => this.addNote('G7', 'string6')}>G</button>
                        <button class="btn" onClick={() => this.addNote('G#6', 'string6')}>G#</button>
                        <button class="btn" onClick={() => this.addNote('A7', 'string6')}>A</button>
                        <button class="btn" onClick={() => this.addNote('A#6', 'string6')}>A#</button>
                        <button class="btn" onClick={() => this.addNote('B7', 'string6')}>B</button>
                        <button class="btn" onClick={() => this.addNote('C6', 'string6')}>C</button>
                        <button class="btn" onClick={() => this.addNote('C#6', 'string6')}>C#</button>
                        <button class="btn" onClick={() => this.addNote('D7', 'string6')}>D</button>
                        <button class="btn" onClick={() => this.addNote('D#6', 'string6')}>D#</button>
                        <button class="btn" onClick={() => this.addNote('E8', 'string6')}>E</button>
                    </div>
                </div>
                <div id="noteList">

                </div>

            </div>
        )
    }

    renderList(){
        return this.state.notesToSend.map(note => (
            <li>{note.note}</li>
        ));
    }

    addNote(note, stringId){
        this.state.notesToSend.forEach(function (item){
            if(item.stringId === stringId){
                item.note = note;
            }
        });
        var test = $('#noteList');
        var tes2= this.renderList().toString();
        test[0].append(this.renderList());
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