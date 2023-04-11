import streamlit as st  # pip install streamlit


### Creation des fonctions et procedures


def hidePage(number):
    style = f"""
    <style>
    div.css-6qob1r.e1fqkh3o3 > div.css-79elbk.e1fqkh3o10 > ul > li:nth-child({number}){{display: none;}}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def showPage(number):
    style = f"""
    <style>
    div.css-6qob1r.e1fqkh3o3 > div.css-79elbk.e1fqkh3o10 > ul > li:nth-child({number}){{display: block;}}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def hideAllPages():
    style = """
    <style>
    div.css-6qob1r.e1fqkh3o3 > div.css-79elbk.e1fqkh3o10 > ul > li{
    display: none;
    }
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def showAllPages():
    style = """
    <style>
    div.css-6qob1r.e1fqkh3o3 > div.css-79elbk.e1fqkh3o10 > ul > li{
    display: block;
    }
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def hideAllPagesExcept(number):
    style = f"""
    <style>
    div.css-6qob1r.e1fqkh3o3 > div.css-79elbk.e1fqkh3o10 > ul > li:nth-child({number}){{display: block;}}
    div.css-6qob1r.e1fqkh3o3 > div.css-79elbk.e1fqkh3o10 > ul > li:not(:nth-child({number})){{display: none;}}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def showAllPagesExcept(number):
    style = f"""
    <style>
    div.css-6qob1r.e1fqkh3o3 > div.css-79elbk.e1fqkh3o10 > ul > li:nth-child({number}){{display: none;}}
    div.css-6qob1r.e1fqkh3o3 > div.css-79elbk.e1fqkh3o10 > ul > li:not(:nth-child({number})){{display: block;}}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def hideMadeWithStreamlit():
    style = """
    <style>
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > footer{display:none;}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def showMadeWithStreamlit():
    style = """
    <style>
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > footer{display:block;}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def hideMenu():
    style = """
    <style>
    #root > div:nth-child(1) > div.withScreencast > div > div > header{display:none;}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def hideSideBar():
    style = """
    <style>
    [data-testid="collapsedControl"] {
        display: none
    }
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def showSideBar():
    style = """
    <style>
    [data-testid="collapsedControl"] {
        display: block
    }
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def addFont(font):
    style = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family={font}&display=swap');
    body {{font-family: '{font}', sans-serif;}}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def avatarImg(img):
    html = f"""
    <style>
    .avatar {{
    vertical-align: middle;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    }}
    </style>
    <img src="{img}" alt="Avatar" class="avatar">
    """


def h1(text):
    st.markdown(
        f'<h1 style="text-align: center;font-family:Nunito; font-size:50pt">{text}</h1>',
        unsafe_allow_html=True,
    )


def loadDaisyUI():
    html = """
    <link href="https://cdn.jsdelivr.net/npm/daisyui@2.51.5/dist/full.css" rel="stylesheet" type="text/css" />
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2/dist/tailwind.min.css" rel="stylesheet" type="text/css" />
    <script src="https://cdn.tailwindcss.com"></script>
    """
