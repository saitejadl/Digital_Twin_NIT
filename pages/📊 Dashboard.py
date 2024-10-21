import folium
from folium.plugins import Draw
import streamlit as st
from streamlit_folium import st_folium
import random
import numpy as np
import pandas as pd
import time

st.set_page_config(page_title="NIREEKSHAN - Dashboard",page_icon="📊",layout="wide", initial_sidebar_state="collapsed", menu_items=None)
_, _, logout= st.columns([5,5,1])
if logout.button("Logout"):
    st.session_state['password']=None
    st.session_state['user_name']=None
    del st.session_state['password']
    del st.session_state['user_name']
    st.switch_page(rf"🔓Login.py")
    st.rerun()

if st.session_state.get('password')!=None:
    st.sidebar.info("🔑SIGNED IN")
    if st.session_state.get('loc')!=None:
        st.title(st.session_state['loc']+" Analytics")
        x1,x2 = st.columns([1,2])
        y1,y2 = st.columns([2,1])
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Load Capacity", "Bearing Capacity", "Yield Strength"])
        x1.line_chart(chart_data)
        x2.line_chart(chart_data, x="a", y=["b", "c"], color=["#FF0000", "#0000FF"])
        st.scatter_chart(chart_data,x='a',y=['b', "c"],size='c',color=['#FF0000', '#0000FF'])# Optional)
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Deterioration rate", "Rework rate", "Accident rate"])
        st.bar_chart(chart_data)
    else:
            st.header("Please select any Architecture from Architecture page and come back here for a 3d view of the architecture")
            st.warning("NO SITE WAS SELECTED")
else:
    st.header("Please signin and visit this page again to view the owned assets")
    st.info("Needed Signin for authentication redirecting to signin page in few seconds")
    time.sleep(10)
    st.switch_page(rf"🔓Login.py")
