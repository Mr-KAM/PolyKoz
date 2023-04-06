import streamlit as st
import pandas as pd
from hackst import *

code_html="""
<style type="text/css">
.add {
  width: 84px;
  height: 84px;
  position: fixed;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  transform: scale(0.5);
  transform-origin: 50% 50%;
  transition: transform 0.4s ease;
  left: 10%;
  bottom: 5%;
}
.add a {
  display: block;
  position: relative;
  width: 50%;
  padding-bottom: 50%;
  background: #5628EE;
  -webkit-backface-visibility: hidden;
  transition: border-radius 0.3s ease, transform 0.2s ease;
}
.add a svg {
  display: block;
  width: 14px;
  height: 14px;
  position: absolute;
  left: 50%;
  top: 50%;
  margin: -7px 0 0 -7px;
  opacity: 0;
  fill: #fff;
  transform: scale(0.6) rotate(-45deg);
  transition: all 0.15s ease;
  -webkit-backface-visibility: hidden;
}
.add a:nth-child(1) {
  border-radius: 8px 0 0 0;
}
.add a:nth-child(2) {
  border-radius: 0 0 0 8px;
}
.add a:nth-child(3) {
  border-radius: 0 8px 0 0;
}
.add a:nth-child(4) {
  border-radius: 0 0 8px 0;
}
.add:before, .add:after {
  content: "";
  width: 28px;
  height: 6px;
  border-radius: 3px;
  background: #fff;
  position: absolute;
  left: 50%;
  top: 50%;
  display: block;
  z-index: 1;
  transform-origin: 50% 50%;
  transition: transform 0.25s ease;
}
.add:before {
  transform: translate(-50%, -50%) scaleY(0.76);
}
.add:after {
  transform: translate(-50%, -50%) rotate(90deg) scaleY(0.76);
}
.add:hover {
  transform: scale(1) rotate(45deg);
  transition: transform 0.4s ease 0.1s;
}
.add:hover:before {
  transform: translate(-50%, -50%) scaleY(0.76) scaleX(3);
}
.add:hover:after {
  transform: translate(-50%, -50%) rotate(90deg) scaleY(0.76) scaleX(3);
}
.add:hover a {
  --scale: 1;
  pointer-events: none;
  border-radius: 50%;
  -webkit-animation: pointerEvent 0s linear forwards 0.4s;
          animation: pointerEvent 0s linear forwards 0.4s;
  transition: border-radius 0.15s ease 0.1s, transform 0.25s ease 0.15s;
}
.add:hover a:nth-child(1) {
  transform: translate(-6px, -6px) scale(var(--scale));
}
.add:hover a:nth-child(2) {
  transform: translate(-6px, 6px) scale(var(--scale));
}
.add:hover a:nth-child(3) {
  transform: translate(6px, -6px) scale(var(--scale));
}
.add:hover a:nth-child(4) {
  transform: translate(6px, 6px) scale(var(--scale));
}
.add:hover a svg {
  opacity: 0.7;
  transition: all 0.3s ease 0.2s;
  transform: scale(1) rotate(-45deg);
}
.add:hover a:hover {
  --scale: .92;
  transition: border-radius 0.2s ease 0.1s, transform 0.25s ease 0s;
}
.add:hover a:hover svg {
  opacity: 1;
  transition: all 0.3s ease 0s;
}

@-webkit-keyframes pointerEvent {
  100% {
    pointer-events: auto;
  }
}

@keyframes pointerEvent {
  100% {
    pointer-events: auto;
  }
}
html {
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
}

* {
  box-sizing: inherit;
}
*:before, *:after {
  box-sizing: inherit;
}

body {
  min-height: 100vh;
  font-family: Roboto, Arial;
  color: #ADAFB6;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #F5F9FF;
}
body .dribbble {
  position: fixed;
  display: block;
  right: 20px;
  bottom: 20px;
}
body .dribbble img {
  display: block;
  height: 28px;
}
</style>
<div class="add">
    <a href="#" target="_self">
        <svg>
            <use xlink:href="#fileIcon">
        </svg>
    </a>
    <a href="image" target="_self">
        <svg>
            <use xlink:href="#imageIcon">
        </svg>
    </a>
    <a href="code" target="_self">
        <svg>
            <use xlink:href="#mailIcon">
        </svg>
    </a>
    <a href="message" target="_self">
        <svg>
            <use xlink:href="#chatIcon">
        </svg>
    </a>
</div>
        
<svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
    <symbol xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" id="fileIcon">
        <path stroke="none" d="M14,0H3A1,1,0,0,0,2,1V23a1,1,0,0,0,1,1H21a1,1,0,0,0,1-1V8H15a1,1,0,0,1-1-1ZM5,17H19v2H5Zm0-5H19v2H5Zm6-3H5V7h6Z"></path>
        <polygon stroke="none" points="21.414 6 16 6 16 0.586 21.414 6"></polygon>
    </symbol>
    <symbol xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" id="imageIcon">
        <circle stroke="none" cx="9" cy="8" r="2"></circle>
        <path stroke="none" d="M23,1H1C0.448,1,0,1.447,0,2v20c0,0.553,0.448,1,1,1h22c0.552,0,1-0.447,1-1V2C24,1.447,23.552,1,23,1z M22,3v12l-5-5l-6,7l-5-4l-4,4V3H22z"></path>
    </symbol>
    <symbol xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" id="mailIcon">
        <path stroke="none" d="M21,2H3A3,3,0,0,0,0,5V19a3,3,0,0,0,3,3H21a3,3,0,0,0,3-3V5A3,3,0,0,0,21,2ZM8.207,15.207l-2.5,2.5a1,1,0,0,1-1.414-1.414l2.5-2.5Zm11.5,2.5a1,1,0,0,1-1.414,0l-2.5-2.5,1.414-1.414,2.5,2.5A1,1,0,0,1,19.707,17.707Zm0-10-7,7a1,1,0,0,1-1.414,0l-7-7A1,1,0,0,1,5.707,6.293L12,12.586l6.293-6.293a1,1,0,1,1,1.414,1.414Z"></path>
    </symbol>
    <symbol xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" id="chatIcon">
        <g stroke="none">
            <path d="M21.965,9.575C21.604,14.821,16.384,19,10,19c-0.465,0-0.931-0.026-1.394-0.072 c2.013,1.586,4.939,2.376,7.946,1.967L22,23.618v-5.215c1.293-1.243,2-2.791,2-4.403C24,12.373,23.277,10.822,21.965,9.575z"></path>
            <path d="M10,1C4.477,1,0,4.582,0,9c0,1.797,0.75,3.45,2,4.785V19l4.833-2.416C7.829,16.85,8.892,17,10,17 c5.523,0,10-3.582,10-8S15.523,1,10,1z"></path>
        </g>
    </symbol>
</svg>
            
<!-- dribbble -->
<a class="dribbble" href="https://dribbble.com/shots/5419580-Add-Button-hover-animation" target="_blank"><img src="https://cdn.dribbble.com/assets/dribbble-ball-mark-2bd45f09c2fb58dbbfb44766d5d1d07c5a12972d602ef8b32204d28fa3dda554.svg" alt=""></a>
"""




st.markdown(code_html, unsafe_allow_html=True)

st.title("IMAGE")

hideMadeWithStreamlit()
hidePage(1)
# hideSideBar()
# addFont("Gluten")