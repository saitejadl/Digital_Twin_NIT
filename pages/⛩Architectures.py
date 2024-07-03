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
# from streamlit_lottie import st_lottie
# import time

st.set_page_config(page_title="NIREEKSHAN - Architecture",page_icon="⛩",layout="wide", initial_sidebar_state="collapsed", menu_items=None)

# st.session_state['last_object_clicked'] = False
if st.session_state.get('password')!=None:
    st.sidebar.info("🔑SIGNED IN")
    _,greet,_ = st.columns([2,2,1])
    greet.title(f"Hi {st.session_state['user_name'].title()}")
    st.write("Architectures Map")
    loc = {
    "Kandappanchal Arch Bridge": [11.442902968845491, 76.06647154478142],
    "Feroke Railway bridge": [11.180595768970802, 75.82888960998298],
    "Areekode Bridge": [11.240843405630452, 76.04558893998195],
    "Kuniyil Kadavu Bridge": [11.385219648663687, 75.7452814852894]
    }
    des = {
    "Kandappanchal Arch Bridge": "The Kandappanchal Arch Bridge is noted as the only arch bridge in Kerala, and it’s unique because it doesn’t have a concrete support beam underneath. Instead, the support arch is visible on top of the bridge. It’s recognized as the largest arch bridge in South India and is quite a beautiful structure",
    "Feroke Railway bridge": 'The Feroke Railway Bridge is a historical structure located in Feroke, Kerala. It was built by the British in 1883 and has served as a major link between Chaliyam and Kozhikode1. This bridge is part of the rich history of Feroke, a municipality that was once considered by Tipu Sultan as a potential capital in Malabar2. The old bridge stands as a testament to the engineering skills of the time and has recently undergone a facelift to preserve its integrity',
    "Areekode Bridge": "The Areekode Bridge is a notable landmark in the town of Areekode (officially Areacode), which is situated on the banks of the Chaliyar River in the Malappuram district of Kerala, India1. While there isn’t a dedicated Wikipedia page for the Areekode Bridge itself, the Wikipedia page for Areekode provides information about the town and its features, including the bridge",
    "Kuniyil Kadavu Bridge": "The Kuniyil Kadavu Bridge is an important structure in Kozhikode district, Kerala. It connects the town of Atholi to National Highway 66 and is recognized as the longest bridge in the district1. The bridge is part of the state highway to Kuttiyadi and plays a significant role in the connectivity of the region"
    }
    st.session_state['locations'] = loc
    m = folium.Map(location=[11.442902968845491, 76.06647154478142], zoom_start=5)
    Draw(export=True).add_to(m)

    for i,j in list(zip(loc.keys(),loc.values())):
        #icon=folium.Icon(color=random.choice(['red', 'blue', 'green', 'yellow']))
        folium.Marker(j, popup=f"<span style='font-size: 10px; color: gray'>{i}\n{j}</span>", tooltip=i).add_to(m)
    output = st_folium(m, width='100%', height=650, returned_objects=["last_object_clicked"])
    st.session_state['last_object_clicked'] = output
    if output.get('last_object_clicked')!=None:
        coordinates = [output["last_object_clicked"]['lat'], output["last_object_clicked"]['lng']]
        st.session_state['loc'] = list(loc.keys())[list(loc.values()).index(coordinates)]
        col1, col2, col3= st.columns(3)
        col1.metric(label="***Lattitude***", value=output["last_object_clicked"]['lat'])
        col2.metric(label="***Longitude***", value=output["last_object_clicked"]['lng'])
        col3.metric(label="***Name***", value=next((k for k, v in loc.items() if v == [output["last_object_clicked"]['lat'],output["last_object_clicked"]['lng']]), None))
        st.write(des[st.session_state['loc']])
        # des[st.session_state['loc']]
            #"""r"Kuniyil Kadavu Bridge/ C.H. MOHAMMED KOYA BRIDGE.. This is the longest bridge in Calicut district. The bridge connects Chemananchery and Atoli Panchayath. \
        #It is constructed across Akalapuzha. After the construction of this bridge people from Atoli can reach Thiruvangoor by travelling 2.4 kms ,hence a saving of 16 kms. \
        #This bridge has 10 spans of 26.60m each and width of 7.50 m. Also it connects NH17 & SH 38. The full mark goes to former PWD Minister mr.P.K.K. BAVA. in realising this bridge.")"""
        col = st.columns([2,1,2])
        with col[1]:
            if st.button("3D View",type="primary"):
                st.switch_page(rf"pages/🌍3d view.py")
    else:
        _,ask,_ = st.columns([2,2,1])
        ask.write(r"Please select any geographical location to view the architecture")
else:
    st.header("Please signin and visit this page again to view the owned assets")
    st.info("Needed Signin for authentication")