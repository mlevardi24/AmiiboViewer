import streamlit as st
import requests
import json
from PIL import Image
import urllib.request 

st.markdown("<center><h1>Nintendo Amiibo Viewer</h1><br><br></center>", unsafe_allow_html=True)

data = requests.get("https://www.amiiboapi.com/api/amiibo/").json()

if "CharFilter" not in st.session_state:
    st.session_state["CharFilter"] = ""

if "GameFilter" not in st.session_state:
    st.session_state["GameFilter"] = ""

if "AmiiboFilter" not in st.session_state:
    st.session_state["AmiiboFilter"] = ""

gameSeries = []
amiiboSeries = []
characters = []

for i in range(0, len(data['amiibo'])):
    check = data['amiibo'][i]["gameSeries"] not in gameSeries

    if check == True:
        gameSeries.append(data['amiibo'][i]["gameSeries"])

##st.write(gameSeries)

for i in range(0, len(data['amiibo'])):
    check = data['amiibo'][i]["amiiboSeries"] not in amiiboSeries

    if check == True:
        amiiboSeries.append(data['amiibo'][i]["amiiboSeries"])

##st.write(amiiboSeries)
        
for i in range(0, len(data['amiibo'])):
    check = data['amiibo'][i]["character"] not in characters

    if check == True:
        characters.append(data['amiibo'][i]["character"])

##st.write(characters)

gameSeries = sorted(gameSeries)
amiiboSeries = sorted(amiiboSeries)
characters = sorted(characters)

gameSeries.insert(0, "ANY")
amiiboSeries.insert(0, "ANY")
characters.insert(0, "ANY")

col1, col2, col3 = st.columns([1,4,1])

with col2:
    charactersSelect = st.selectbox("Character", characters)
    col1a, col2a = st.columns(2)
    with col1a:
        amiiboSeriesSelect = st.selectbox("Amiibo Series", amiiboSeries)
    with col2a:
        gameSeriesSelect = st.selectbox("Game Series", gameSeries)

with st.container(border=True):
    if charactersSelect != "ANY":
        st.session_state["CharFilter"] = charactersSelect
    else:
        st.session_state["CharFilter"] = ""
    if gameSeriesSelect != "ANY":
        st.session_state["GameFilter"] = gameSeriesSelect
    else:
        st.session_state["GameFilter"] = ""
    if amiiboSeriesSelect != "ANY":
        st.session_state["AmiiboFilter"] = amiiboSeriesSelect
    else:
        st.session_state["AmiiboFilter"] = ""

    for i in range(1,len(amiiboSeries)):
        if st.session_state["AmiiboFilter"] == amiiboSeries[i] or len(st.session_state["AmiiboFilter"]) == 0:
            inc = 6
            data = requests.get("https://www.amiiboapi.com/api/amiibo/?amiiboSeries={0}&character={1}&gameseries={2}".format(amiiboSeries[i],st.session_state['CharFilter'],st.session_state['GameFilter'])).json()
            if len(data['amiibo']) != 0:
                st.markdown("<h4>{}</h4>".format(amiiboSeries[i]), unsafe_allow_html=True)
                while True:
                    col1, col2, col3, col4, col5, col6 =st.columns(6)
                    with col1:
                        try:
                            with st.container(border=True):
                                urllib.request.urlretrieve(data['amiibo'][inc - 6]['image'], "cewl.png") 
                                img = Image.open("cewl.png") 
                                imgR = img.resize((70,95))
                                st.image(imgR)
                                st.markdown("""
                                <div class='w3-container' style='height:65px;overflow:scroll'>
                                    <p>{0}</p>
                                </div>
                                """.format(data['amiibo'][inc - 6]['name']), unsafe_allow_html=True)
                        except:
                            break
                    with col2:
                        try:
                            with st.container(border=True):
                                urllib.request.urlretrieve(data['amiibo'][inc - 5]['image'], "cewl.png") 
                                img = Image.open("cewl.png") 
                                imgR = img.resize((70,95))
                                st.image(imgR)
                                st.markdown("""
                                <div class='w3-container' style='height:65px;overflow:scroll'>
                                    <p>{0}</p>
                                </div>
                                """.format(data['amiibo'][inc - 5]['name']), unsafe_allow_html=True)
                        except:
                            break
                    with col3:
                        try:
                            with st.container(border=True):
                                urllib.request.urlretrieve(data['amiibo'][inc - 4]['image'], "cewl.png") 
                                img = Image.open("cewl.png") 
                                imgR = img.resize((70,95))
                                st.image(imgR)
                                st.markdown("""
                                <div class='w3-container' style='height:65px;overflow:scroll'>
                                    <p>{0}</p>
                                </div>
                                """.format(data['amiibo'][inc - 4]['name']), unsafe_allow_html=True)
                        except:
                            break
                    with col4:
                        try:
                            with st.container(border=True):
                                urllib.request.urlretrieve(data['amiibo'][inc - 3]['image'], "cewl.png") 
                                img = Image.open("cewl.png") 
                                imgR = img.resize((70,95))
                                st.image(imgR)
                                st.markdown("""
                                <div class='w3-container' style='height:65px;overflow:scroll'>
                                    <p>{0}</p>
                                </div>
                                """.format(data['amiibo'][inc - 3]['name']), unsafe_allow_html=True)
                        except:
                            break
                    with col5:
                        try:
                            with st.container(border=True):
                                urllib.request.urlretrieve(data['amiibo'][inc - 2]['image'], "cewl.png") 
                                img = Image.open("cewl.png") 
                                imgR = img.resize((70,95))
                                st.image(imgR)
                                st.markdown("""
                                <div class='w3-container' style='height:65px;overflow:scroll'>
                                    <p>{0}</p>
                                </div>
                                """.format(data['amiibo'][inc - 2]['name']), unsafe_allow_html=True)
                        except:
                            break
                    with col6:
                        try:
                            with st.container(border=True):
                                urllib.request.urlretrieve(data['amiibo'][inc - 1]['image'], "cewl.png") 
                                img = Image.open("cewl.png") 
                                imgR = img.resize((70,95))
                                st.image(imgR)
                                st.markdown("""
                                <div class='w3-container' style='height:65px;overflow:scroll'>
                                    <p>{0}</p>
                                </div>
                                """.format(data['amiibo'][inc - 1]['name']), unsafe_allow_html=True)
                        except:
                            break
                    inc = inc + 6
  

