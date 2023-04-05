# Import Library
import streamlit as st
from PIL import Image
import qrcode
import os
import numpy as np
import random as rd
import time


# Configurations du code QR
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=3)

# Creation d'un Dossier pour les Codes
path = "./codes_QR"
isdir = os.path.isdir(path)
if not isdir:
    os.mkdir('codes_QR')


# Foncion pour charger le code
def charger_code(img):
    qr_img = Image.open(img)
    return qr_img


# Fonction principale
def main():
    menu = ["Texte en QR"]

    choice = st.sidebar.selectbox("Menu", menu)

   
st.subheader("Texte en QR")
idx = rd.randint(1,100)
        # Saisie de texte
with st.form(key="myqr_form"):
        st.write('---')
        st.header("CODE QR")
        Nom = st.text_input("Quel est votre nom ?")
        Prenom = st.text_input("Quel est votre prenom ?")
        Age = st.number_input("Entrez votre age")
        text_contents = f'Votre Identifiant est :{str(23)+Nom+str(idx)} Nom:{Nom}; Prenom:{Prenom}; Age:{Age}'
        


        submit_button = st.form_submit_button("Générer code QR")

        # Format de la mise en page
        if submit_button:
            c1, c2 = st.columns(2)
            with c1:
                # Ajout du texte
                qr.add_data(text_contents)

                # Générer QR
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")

                # Nom du fichier image
                date_time = time.strftime("%Y%m%d-%H%M%S")
                img_filename = "QR_Image_{}.png".format(date_time)
                img_path = os.path.join("codes_QR", img_filename)
                img.save(img_path)

                # Charger image QR
                img_chargee = charger_code(img_path)
                st.image(img_chargee)
            with c2:
                st.info("Votre Texte")
                st.write(text_contents)

print(text_contents)
        


if __name__ == "__main__":
    main()