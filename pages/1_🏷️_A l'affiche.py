import streamlit as st
from hackst import *

hidePage(1)
hideMenu()
hideMadeWithStreamlit()
addFont("Nunito")

h1("A l'affiche")

expander = st.expander("See explanation")
expander.write(
    "The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're *guaranteed* to be random."
)
expander.image("https://static.streamlit.io/examples/dice.jpg")
