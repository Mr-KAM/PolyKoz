import streamlit as st
from streamlit_chat import message
from transformers import BlenderbotTokenizer
from transformers import BlenderbotForConditionalGeneration
from hackst import *

hidePage(1)
hideMenu()
hideMadeWithStreamlit()
addFont("Nunito")


def generate_answer():
    tokenizer, model = get_models()
    user_message = st.session_state.input_text
    inputs = tokenizer(st.session_state.input_text, return_tensors="pt")
    result = model.generate(**inputs)
    message_bot = tokenizer.decode(
        result[0], skip_special_tokens=True
    )  # .replace("<s>", "").replace("</s>", "")

    st.session_state.history.append({"message": user_message, "is_user": True})
    st.session_state.history.append({"message": message_bot, "is_user": False})


@st.cache_resource
def get_models():
    # it may be necessary for other frameworks to cache the model
    # seems pytorch keeps an internal state of the conversation
    model_name = "facebook/blenderbot-400M-distill"
    tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
    model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model


if "history" not in st.session_state:
    st.session_state.history = []


tabs = ("Perso ✌🏾", "Groupes ✊🏾")

perso, groupe = st.tabs(tabs)

with perso:
    contact_perso = st.selectbox(
        "Pote de discussion", ("Email", "Home phone", "Mobile phone")
    )

    message("My message")
    message("Hello bot!", is_user=True)  # align's the message to the right

    st.text_input("Envoyer un message:", key="input_text", on_change=generate_answer)

with groupe:
    groupe = st.text_input("Groupe de discussion:", key="groupe")
    # message("My message")
    # message("Hello bot!", is_user=True)  # align's the message to the right

    # st.text_input("Envoyer un message:", key="input_text", on_change=generate_answer)
