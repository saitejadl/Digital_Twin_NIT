# import folium
# # from folium.plugins import Draw
# import streamlit as st
# from streamlit_folium import st_folium
# import time

# st.set_page_config(page_title="NIREEKSHAN - PROJECT DIGITAL TWIN",page_icon="🌎",layout="wide", initial_sidebar_state="collapsed" if st.session_state.get("logged_in")!=True else "auto")

# st.logo('assets/Neerakshan_logo.png', link='https://samudra-digital-twin.streamlit.app/', icon_image='assets/Neerakshan_logo.png')
# def stream_data(heading):
#     if st.session_state.get('user_name') == None:
#         heading=heading
#     else:
#         heading = f"Hello {st.session_state.get('user_name')}"
#     for letter in [x for x in heading]:
#         yield letter + ""
#         time.sleep(0.01)
# _, __, ___= st.columns([3,2,3])

# __.image('assets/Neerakshan_logo.png', caption=' ')
# __.write_stream(stream_data("""THE BEST WAY TO PREDICT THE FUTURE \n IS TO CREATE IT."""))
# # c1,c2,c3 = st.columns([1,3,1])
# # c2.header("NIREEKSHAN - PROJECT DIGITAL TWIN")
# # c2.write_stream(stream_data("THE BEST WAY TO PREDICT THE FUTURE IS TO CREATE IT."))

# u_p = {"prateek":"0000",
#        "teja":"1234",
#        "chinmay":"4321",
#        "haneena":"1234",
#        "kavya":"1234",
#        "subham":"1234"}
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
#                             # st.sidebar.page_link("pages/⛩Site_Map.py")
#                             st.switch_page(rf"pages/⛩Site_Map.py")
#                         elif password!='':
#                             st.error("Invalid Password")      
#                     elif user_name!='':
#                         st.error("Invalid Username")
#             # if st.session_state.get('password')!=None and st.session_state.get('password')==True:
#             #     st.switch_page(rf"pages\⛩Site_Map.py")

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




import streamlit as st
import time

st.set_page_config(page_title="NIREEKSHAN - PROJECT DIGITAL TWIN",page_icon="🌎",layout="wide", initial_sidebar_state="collapsed" if st.session_state.get("logged_in")!=True else "auto")

st.logo('assets/Neerakshan_logo.png', link='https://samudra-digital-twin.streamlit.app/', icon_image='assets/Neerakshan_logo.png')

page_bg_img = """
<style>
[data-testid = "stAppViewContainer"] {background-image: url("https://images.unsplash.com/photo-1680071523030-802bb5195a30?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"); background-size: cover;}
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(125, 125, 125, 0.4); /* Adjust the opacity as needed */
    z-index: 0;
}
[data-testid = "stHeader"] {background-color: rgba(0, 0, 0, 0);}
[data-testid = "stToolbar"] {{ right: 2rem;}}
</style>
              """
st.markdown(page_bg_img, unsafe_allow_html=True)

def stream_data(heading):
    if st.session_state.get('user_name') == None:
        heading=heading
    else:
        heading = f"Hello {st.session_state.get('user_name')}"
    for letter in [x for x in heading]:
        yield letter + ""
        time.sleep(0.01)

_, __, ___= st.columns([3,2,3])

__.image('assets/Neerakshan_logo.png', caption=' ')

__.write_stream(stream_data("""THE FUTURE OF DATA-DRIVEN DECISION MAKING"""))
# c1,c2,c3 = st.columns([1,3,1])
# c2.header("NIREEKSHAN - PROJECT DIGITAL TWIN")
# c2.write_stream(stream_data("THE BEST WAY TO PREDICT THE FUTURE IS TO CREATE IT."))

u_p = {"prateek":"0000",
       "teja":"1234",
       "chinmay":"4321",
       "haneena":"1234",
       "kavya":"1234",
       "subham":"1234",
       "shaan":"4862",
       "alan":"0018"}


if st.session_state.get('password') == None:
    i,j,h = st.columns([1,2,1])
    with j:
        with st.form("signin", border=True,clear_on_submit=False):
            x,y,z = st.columns([1,2,1])
            y.markdown('<h2 style="color:white;">SIGNIN</h2>', unsafe_allow_html=True)
            a,b,c = st.columns([1,2,1])
            d,e,f = st.columns([1,2,1])
            g,h,i = st.columns([1,2,1])
            user_name = b.text_input(' ', value="")
            b.markdown('<h6 style="color:white;">Username</h6>', unsafe_allow_html=True)
            password = e.text_input('', value="", type="password")
            e.markdown('<h6 style="color:white;">Password</h6>', unsafe_allow_html=True)
            e.markdown("***")

            with h:
                if st.form_submit_button("signin", type="primary"):
                    if user_name in u_p.keys():
                        st.session_state['user_name'] = user_name
                        if password==u_p[user_name]:
                            st.session_state['password'] = password==u_p[user_name]
                            st.sidebar.info("🔑SIGNED IN ")
                            h.success("SIGNED IN SUCCESSFULLY")
                            st.session_state.logged_in = True
                            # st.sidebar.page_link("pages/⛩Site_Map.py")
                            st.switch_page(rf"pages/⛩Site_Map.py")
                        elif password!='':
                            st.error("Invalid Password")      
                    elif user_name!='':
                        st.error("Invalid Username")
            # if st.session_state.get('password')!=None and st.session_state.get('password')==True:
            #     st.switch_page(rf"pages\⛩Site_Map.py")

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
