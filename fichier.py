### Imporation des modules

import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
from deta import Deta  # pip install deta
from hackst import *
from streamlit_extras.switch_page_button import switch_page
import os, sys

st.set_page_config(initial_sidebar_state="collapsed")
parentdir = os.path.dirname(__file__)
sys.path.insert(0, parentdir)

### Déclaration de variables et constantes
deta = Deta(st.secrets["data_key"])

print(deta)
names = ["John Smith", "Rebecca Briggs"]
usernames = ["jsmith", "rbriggs"]

userdata = [
    {
        "email": "jsmith@gmail.com",
        "name": "John Smith",
        "password": "$2b$12$Ae/rIEVfbnQZrG24x/gFoetbgjhVfbi5UIQXd2xLU6mibtk4pdNHO",
    },
    {
        "email": "rbriggs@gmail.com",
        "name": "Rebecca Briggs",
        "password": "$2b$12$waR.dgr/wUI0Y4LJ4UtiZ.oM/qSsnnEiK9uCS8aVT7q5IKvVSPqKa",
    },
]
passwords = ["123", "456"]

zipbObj = zip(usernames, userdata)
# print(dict(zipbObj))

# print(config)


hideSideBar()
hidePage(1)
hideMenu()
hideMadeWithStreamlit()
addFont("Gluten")

st.image("https://inphb.ci/2/src/img/logo.gif")
# hashed_passwords = stauth.Hasher(passwords).generate()
# print(hashed_passwords)
authenticator = stauth.Authenticate(
    {"usernames": dict(zipbObj)},
    "some_cookie_name",
    "some_signature_key",
    cookie_expiry_days=30,
)

name, authentication_status, username = authenticator.login("Connexion", "main")

if authentication_status == True:
    switch_page("A_l'affiche")

### Programme principale d'authentication
