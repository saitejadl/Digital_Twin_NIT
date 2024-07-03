import folium
from folium.plugins import Draw
import streamlit as st
from streamlit_folium import st_folium
# import pyvista as pv
# from stpyvista import stpyvista
# import random
# import requests
# import json
# from pathlib import Path
# from PIL import Image
# import numpy as np
# import pandas as pd
# from streamlit_lottie import st_lottie
# import time
st.set_page_config(page_title="NIREEKSHAN - 3D View",page_icon="🌎",layout="wide", initial_sidebar_state="collapsed", menu_items=None)

if st.session_state.get('password')!=None:
    st.sidebar.info("🔑SIGNED IN")
    if st.session_state.get('last_object_clicked') != None:
        if st.session_state.get('last_object_clicked')['last_object_clicked'] != None:
            output = st.session_state['last_object_clicked']
            loc = st.session_state['locations']
            progress_text = "Operation in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(3)
            my_bar.empty()
            loc = {"Kandappanchal Arch Bridge": """<div class="sketchfab-embed-wrapper"> <iframe title="Bridge" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share width="100%" height="100%" src="https://sketchfab.com/models/545a57d9785443bca9b135da2e497bc0/embed?autostart=1&preload=1&ui_theme=dark"> </iframe></div>""",
                    "Feroke Railway bridge": """<div class="sketchfab-embed-wrapper"> <iframe title="NYC, The High Bridge" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share width="100%" height="800" src="https://sketchfab.com/models/1a98cc4fe0064c009f4c2da35f0fc232/embed?autostart=1&preload=1&transparent=1&ui_theme=dark"> </iframe></div>""",
                    "Areekode Bridge": """<div class="sketchfab-embed-wrapper"> <iframe title="Martha McClean Bridge" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share width="100%" height="800" src="https://sketchfab.com/models/b025b69e36874fac8886bdb1bd17c2e3/embed?autostart=1&preload=1&ui_theme=dark"> </iframe> </div>""",
                    "Kuniyil Kadavu Bridge": """<div class="sketchfab-embed-wrapper"> <iframe title="Bridge" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share width="100%" height="800" src="https://sketchfab.com/models/b95a1cf88cae49ada50f9264cf51d43d/embed?autostart=1&preload=1&ui_theme=dark"> </iframe> </div>"""
                    }
            # if st.session_state.get('last_object_clicked')['last_object_clicked'] == 
            html = loc[st.session_state['loc']]
            st.markdown(html, unsafe_allow_html=True)
            st.write("---")

            # uploaded_file = st.sidebar.file_uploader("Upload a 3D model", type=["obj", "stl", "ply"])
            # if uploaded_file==None:
            #     uploaded_file = rf'C:\TEJA\Project2\3d models\Gemstone.ply'
            # else:
            #     uploaded_file = uploaded_file.name
            # plotter = pv.Plotter(window_size=[1000,500])
            # mesh = pv.read(uploaded_file)
            # plotter.clear()
            # plotter.add_mesh(mesh, cmap='rgb', line_width=1, label="Kallai Bridge")
            # plotter.add_scalar_bar()
            # plotter.add_title("Gem", color="black", font_size=14)
            # plotter.view_isometric()
            # plotter.background_color = 'lightgray'
            # stpyvista(plotter, use_container_width=True, panel_kwargs=dict(orientation_widget = True),horizontal_align='center')
            col4, col5, col6= st.columns(3)
            col4.metric(label= "AREA in mtr sq", value="96747", delta="-676")
            col5.metric(label="MASS in lbs", value="757889", delta="56")
            col6.metric(label="VOLUME in mtr cu", value="645465 mtcu", delta="-786")
            col7, col8, col9= st.columns(3)
            col7.metric(label="SEVERITY", value="2⭐")
            col8.metric(label="DAMAGE", value="💥10%")
            col9.metric(label="ALERT LEVEL", value="5⚠")
            col = st.columns([2,1,2])
            with col[1]:
                if st.button("Analytics",type="primary"):
                    st.switch_page(rf"pages/📊 Dashboard.py")
                

        else:
            st.header("Please select any Architecture from Architecture page and come back here for a 3d view of the architecture")
            st.warning("NO ARCHITECTURE WAS SELECTED")
            # st.toast(f"Latitude: {output["last_object_clicked"]['lat']} Longitute: {output["last_object_clicked"]['lat']}")
else:
    st.header("Please signin and visit this page again to view the owned assets")
    st.info("Needed Signin for authentication")
