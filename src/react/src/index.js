import React from "react";
import ReactDOM from "react-dom";
import HomePage from './js/components/index/HomePage.jsx';

const wrapper = document.getElementById("index");
wrapper ? ReactDOM.render(<HomePage/>, wrapper): false;