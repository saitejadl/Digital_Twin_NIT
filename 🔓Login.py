# import folium
# from folium.plugins import Draw
# import streamlit as st
# from streamlit_folium import st_folium
# # import pyvista as pv
# # from stpyvista import stpyvista
# # import random
# # import requests
# # import json
# # from pathlib import Path
# # from PIL import Image
# # from streamlit_lottie import st_lottie
# import time


# st.set_page_config(page_title="NIRKEESHAN - PROJECT DIGITAL TWIN",page_icon="🌎",layout="wide", initial_sidebar_state="collapsed" if st.session_state.get("logged_in")!=True else "auto")

# def stream_data(heading):
#     if st.session_state.get('user_name') == None:
#         heading=heading
#     else:
#         heading = f"Hello {st.session_state.get('user_name')}"
#     for letter in [x for x in heading]:
#         yield letter + ""
#         time.sleep(0.01)

# c1,c2,c3 = st.columns([1,3,1])
# c2.header("NIREEKSHAN - PROJECT DIGITAL TWIN")
# c2.write_stream(stream_data("THE BEST WAY TO PREDICT THE FUTURE IS TO CREATE IT."))

# u_p = {"pratheek":"0000",
#        "teja":"1234",
#        "chinmay":"4321",
#        "haneena":"6789",}
# # st.write("##")
# # st.session_state['user_name'] = False
# # st.session_state['password'] = False
# # st.session_state['last_object_clicked']=False

# if st.session_state.get('password') == None:
#     i,j,h = st.columns([1,2,1])
#     with j:
#         with st.form("signin", border=True,clear_on_submit=False):
#             x,y,z = st.columns([1,2,1])
#             y.subheader(':blue[SIGNIN]', anchor='signin')
#             a,b,c = st.columns([1,2,1])
#             d,e,f = st.columns([1,2,1])
#             g,h,i = st.columns([1,2,1])
            
#             user_name = b.text_input('Username', value="")
#             password = e.text_input('Password', value="", type="password")
            
#             with h:
#                 if st.form_submit_button("signin"):
#                     if user_name in u_p.keys():
#                         st.session_state['user_name'] = user_name
#                         if password==u_p[user_name]:
#                             st.session_state['password'] = password==u_p[user_name]
#                             st.sidebar.info("🔑SIGNED IN ")
#                             h.success("SIGNED IN SUCCESSFULLY")
#                             st.session_state.logged_in = True
#                             # st.sidebar.page_link("pages/⛩Architectures.py")
#                             st.switch_page(rf"pages/⛩Architectures.py")
#                         elif password!='':
#                             st.error("Invalid Password")      
#                     elif user_name!='':
#                         st.error("Invalid Username")
# # if st.session_state.get('password')!=None and st.session_state.get('password')==True:
# #     st.switch_page(rf"pages/⛩Architectures.py")

# else:
#     st.info("🔑SIGNED IN SUCCESSFULLY")
#     if st.button("Logout"):
#         st.session_state['password']=None
#         del st.session_state['password']
#         del st.session_state['user_name']
#         st.rerun()

  
#   # url1 = requests.get("https://lottie.host/501a1638-888d-4d34-aa84-513513a38454/m23HdBnRK5.json")
#   # if url1.status_code == 200: url_json1 = url1.json()
#   # else: print("URL ERROR")
#   # st_lottie(url_json1)


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
import time


st.set_page_config(page_title="NIRKEESHAN - PROJECT DIGITAL TWIN",page_icon="🌎",layout="wide", initial_sidebar_state="collapsed" if st.session_state.get("logged_in")!=True else "auto")

def stream_data(heading):
    if st.session_state.get('user_name') == None:
        heading=heading
    else:
        heading = f"Hello {st.session_state.get('user_name')}"
    for letter in [x for x in heading]:
        yield letter + ""
        time.sleep(0.01)

c1,c2,c3 = st.columns([1,3,1])
c2.header("NIREEKSHAN - PROJECT DIGITAL TWIN")
c2.write_stream(stream_data("THE BEST WAY TO PREDICT THE FUTURE IS TO CREATE IT."))

u_p = {"pratheek":"0000",
       "teja":"1234",
       "chinmay":"4321",
       "haneena":"6789",}
# st.write("##")
# st.session_state['user_name'] = False
# st.session_state['password'] = False
# st.session_state['last_object_clicked']=False

if st.session_state.get('password') == None:
    i,j,h = st.columns([1,2,1])
    with j:
        with st.form("signin", border=True,clear_on_submit=False):
            x,y,z = st.columns([1,2,1])
            y.subheader(':blue[SIGNIN]', anchor='signin')
            a,b,c = st.columns([1,2,1])
            d,e,f = st.columns([1,2,1])
            g,h,i = st.columns([1,2,1])
            
            user_name = b.text_input('Username', value="")
            password = e.text_input('Password', value="", type="password")
            
            with h:
                if st.form_submit_button("signin"):
                    if user_name in u_p.keys():
                        st.session_state['user_name'] = user_name
                        if password==u_p[user_name]:
                            st.session_state['password'] = password==u_p[user_name]
                            st.sidebar.info("🔑SIGNED IN ")
                            h.success("SIGNED IN SUCCESSFULLY")
                            st.session_state.logged_in = True
                            # st.sidebar.page_link("pages/⛩Architectures.py")
                            st.switch_page(rf"pages/⛩Architectures.py")
                        elif password!='':
                            st.error("Invalid Password")      
                    elif user_name!='':
                        st.error("Invalid Username")
            # if st.session_state.get('password')!=None and st.session_state.get('password')==True:
            #     st.switch_page(rf"pages\⛩Architectures.py")

else:
    st.info("🔑SIGNED IN SUCCESSFULLY")
    if st.button("Logout"):
        st.session_state['password']=None
        del st.session_state['password']
        del st.session_state['user_name']
        st.rerun()

  
  # url1 = requests.get("https://lottie.host/501a1638-888d-4d34-aa84-513513a38454/m23HdBnRK5.json")
  # if url1.status_code == 200: url_json1 = url1.json()
  # else: print("URL ERROR")
  # st_lottie(url_json1)

