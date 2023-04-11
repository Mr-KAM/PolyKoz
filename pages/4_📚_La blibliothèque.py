import streamlit as st
from hackst import *

hidePage(1)
hideMenu()
hideMadeWithStreamlit()
addFont("Nunito")

from streamlit_modal import Modal

import streamlit.components.v1 as components


modal = Modal("A propos de polykoz", key="modal1")
open_modal = st.button("Open")
if open_modal:
    modal.open()

if modal.is_open():
    with modal.container():
        st.write("Bienvenue ici")

        html_string = """
        <h1>HTML string in RED</h1>
        <script language="javascript">
          document.querySelector("h1").style.color = "red";
        </script>
        """
        components.html(html_string)

        st.write("Some fancy text")
        value = st.checkbox("Check me")
        st.write(f"Checkbox checked: {value}")
