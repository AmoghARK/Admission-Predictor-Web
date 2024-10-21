import streamlit as st
import streamlit_authenticator as stac
import yaml
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
import pickle
import pandas as pd
from yaml import SafeLoader
import datetime
import calendar
import time
import plotly.express as px
from annotated_text import annotated_text
from streamlit_lottie import st_lottie
from  PIL import Image

import requests
from streamlit_lottie import st_lottie_spinner

st.set_page_config(page_title="Admission Predictor", page_icon=":sparkles:" ,layout="centered")

# background set
#def add_bg_from_url():
    #st.markdown(
         #f"""
         #<style>
         #.stApp {{
           #  background-image: url("https://t4.ftcdn.net/jpg/02/98/89/07/360_F_298890723_gxZy7ljKF1pvZcGTpxxUEKPmVXoF2eCZ.jpg");
         #    background-attachment: fixed;
         #    background-size: contain
      #   }}
     #    </style>
         #""",
 ##        unsafe_allow_html=True
  #   )
#add_bg_from_url()


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style2.css")

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            MainMenu {visibility: visible;}
            footer {visibility: visible;}
            footer:after{
                content:"Made by A & R";
                display:block;
                color:grey;
                }
            header {visibility: visible;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


df = pd.read_csv('5colleges.csv')
df.dropna(inplace=True)
df['cutoff'] = df['cutoff'].astype(int)

st.write("""--------------------""")

st.header("""Your stress for finding best college ends here !""")

with st.expander("About us"):
    st.write("---")
    st.header("What I do")
    st.write("##")
    st.write(
        """
         The Admission Predictor Web is used to predict the chances 
                of a student getting admission in his desired college. 
                    web based application can be used to make this process easier, secure.
                        More efficient information's will be achieved through this system.
        """
    )
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("""
                    - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
                    - are working with Excel and found themselves thinking - "there has to be a better way."
                    If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
                    """
                 )
    st.write("[Email>] amoghkelu@gmail.com")
    lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")
    with right_column:
        st_lottie(lottie_hello, height=200, key="coding")


st.write("""----------------------------""")

names = ['Rahul', 'Amogh', 'Sahil', 'Ram']
usernames = ['rpha', 'akel', 'skinj', 'rpar']
passwords = ['abc123', 'def123', 'ghi123', 'jkl123']
hashed_passwords = stac.Hasher(passwords).generate()

authenticator = stac.Authenticate(names, usernames, hashed_passwords, 'Predictor', 'abcdefg', cookie_expiry_days=2)
name, authentication_status, username = authenticator.login("Login", "sidebar")

if authentication_status == False:
    st.error("Username/Password is incorrect")
elif authentication_status == None:
    st.warning("Please enter your username and password😂")
elif authentication_status:
    with st.sidebar:
        col1,col2,col3 = st.columns(3)
        img = Image.open('Predictor.jpeg')
        img = img.resize((400, 400))
        st.image(img)
        authenticator.logout("Logout", "main")
        selected = option_menu(menu_title=f"Welcome", options=['Home','Previous Year Cutoffs','Predictor','Admission form',
                   "FAQ's",'Contact us'],icons=["house-fill","question-square-fill","pencil-fill","bar-chart-fill","droplet-fill",
                   "envelope-fill"], menu_icon="person lines fill",orientation="vertical")

    if selected == "Home":
        """ The Admission Predictor Web is used to predict the chances of a student getting admission in his desired college.
        The core idea of this project is to implement web based application to benefit the students who want to seek admission in their desired college.
        The application will be used by students. In the previous system, all the information has to view in a hard file, or in website. At the same time
        while searching any information about a specific college cut-off or last year cut-off it is too difficult to access and takes a lot of time to
        search the particular website where there is all the information. Hence, in order to overcome this problem a web based application can be used
        to make this process easier, secure. More efficient information's will be achieved through this system."""


    if selected == "Predictor":
        pipe1 = pickle.load(open('pipe1.pkl', 'rb'))
        pipe2 = pickle.load(open('pipe2.pkl', 'rb'))
        pipe3 = pickle.load(open('pipe3.pkl', 'rb'))

        ruparel_castes = ['NT-C', 'SC', 'Open', 'NT-B', 'ST', 'OBC']
        wilson_castes = ['Open']
        kc_castes = ['Open','Sindhi']
        hinduja_castes = ['Open', 'Sindhi']
        colleges = ['College 1','College 2','College 3','College 4']
        streams = ['BSC-IT','BMS','BSC-CS']

        st.title("Admission Predictor")
        selected_stream = st.selectbox("Select Stream",streams)
        if selected_stream == "BSC-IT":
            selected_college = st.selectbox("Select College",colleges)
            if selected_college == 'College 1':
                college_name = "D.G.Ruparel"
                selected_caste = st.selectbox("Select Caste", ruparel_castes)
            if selected_college == 'College 2':
                college_name = "Wilson"
                selected_caste = st.selectbox("Select Caste", wilson_castes)
            if selected_college == 'College 3':
                college_name = "KC"
                selected_caste = st.selectbox("Select Caste", kc_castes)
            if selected_college == 'College 4':
                college_name = "Hinduja"
                selected_caste = st.selectbox("Select Caste", hinduja_castes)
            given_marks = st.number_input('Mathematics Marks')
            input_df = pd.DataFrame({'marks': [given_marks], 'caste': [selected_caste], 'College': [college_name]})
            alk1,alk2 = st.columns(2)
            lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")
            st_lottie(lottie_hello,
                speed=1,
                reverse=False,
                loop=True,
                quality="high",
                height=300,
                width=None,
                key=None
            )

            if st.button('Predict'):
                proba1 = pipe1.predict_proba(input_df)
                proba2 = pipe2.predict_proba(input_df)
                proba3 = pipe3.predict_proba(input_df)
                get_per1 = proba1[0][1]
                get_per2 = proba2[0][1]
                get_per3 = proba3[0][1]
                if get_per1 >= 0.85:
                    st.success('Chances for getting admission in 1st cut-off is {} %'.format(round(get_per1 * 100,2)))
                elif get_per1 <=0.85 and get_per1>=0.60:
                    st.warning('Chances for getting admission in 1st cut-off is {} %'.format(round(get_per1 * 100,2)))
                else:
                    st.error('Chances for getting admission in 1st cut-off is {} %'.format(round(get_per1 * 100,2)))
                if get_per2 >= 0.85:
                    st.success('Chances for getting admission in 2nd cut-off is {} %'.format(round(get_per2 * 100,2)))
                elif get_per2 <=0.85 and get_per2>=0.60:
                    st.warning('Chances for getting admission in 2nd cut-off is {} %'.format(round(get_per2 * 100,2)))
                else:
                    st.error('Chances for getting admission in 2nd cut-off is {} %'.format(round(get_per2 * 100,2)))
                if get_per3 >= 0.85:
                    st.success('Chances for getting admission in 3rd cut-off is {} %'.format(round(get_per3 * 100,2)))
                elif get_per3 <=0.85 and get_per3>=0.60:
                    st.warning('Chances for getting admission in 3rd cut-off is {} %'.format(round(get_per3 * 100,2)))
                else:
                    st.error('Chances for getting admission in 3rd cut-off is {} %'.format(round(get_per3 * 100,2)))

    if selected == "Previous Year Cutoffs":

        df = pd.read_csv('5colleges.csv')
        list = ['1st','2nd','3rd']
        st.title("FYBSc-IT previous cut-offs")
        selected_college_gp = st.selectbox("Select college",['College 1','College 2','College 3','College 4'])
        if selected_college_gp == 'College 1':
            college_name = "D.G.Ruparel"
        if selected_college_gp == 'College 2':
            college_name = "Wilson"
        if selected_college_gp == 'College 3':
            college_name = "KC"
        if selected_college_gp == 'College 4':
            college_name = "Hinduja"
        selected_year = st.selectbox("Choose Year",[2021,2020,2019])
        selected_list = st.multiselect("Which list would you like to see?",list,['1st','2nd','3rd'])
        new_df = df[df['year'] == selected_year]
        new_df = new_df[new_df['College'] == college_name]
        new_df = new_df[new_df['list'].isin(selected_list)]
        new_df.dropna(inplace=True)
        new_df['cutoff'] = new_df['cutoff'].astype(int)
        graph_df = new_df.groupby(['caste', 'list']).max()['cutoff'].reset_index()
        fig = px.bar(graph_df,x='caste',y='cutoff',color='list',barmode="group")
        st.plotly_chart(fig)


        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        # local_css("style/style3.css")
        # Load Animation
        # animation_symbol = "?"
        # st.markdown(
        #    f"""
        #    <div class="snowflake">{animation_symbol}</div>
         #   <div class="snowflake">{animation_symbol}</div>
         #   <div class="snowflake">{animation_symbol}</div>
         #   <div class="snowflake">{animation_symbol}</div>
         #   <div class="snowflake">{animation_symbol}</div>
         #   <div class="snowflake">{animation_symbol}</div>
         #   <div class="snowflake">{animation_symbol}</div>
         #   <div class="snowflake">{animation_symbol}</div>
         #   <div class="snowflake">{animation_symbol}</div>
         #   """,
       #     unsafe_allow_html=True,
       # )

    if selected == "FAQ's":
        #  #8ef-blue, #faa-red, #afa-green, #fea-yellow
        annotated_text(("1) According to predictor when I am able to get admission ?",'Ques','#9A9BAD'))
        annotated_text(("-> If your chances are more than 60% then you have to fill the form",'Ans','#ADD8E6'))
        annotated_text(("2) What is the accuracy of model ?",'Ques','#9A9BAD'))
        annotated_text(("-> Our predictor model has 90% accuracy",'Ans','#ADD8E6'))
        # how do I know my form is submitted
        # If you have other doubts then send email to us from contact us section
        annotated_text(("If you face other problems then send gmail us from contact us section",' ','#808080'))

    if selected == "Contact us":

        contact_form = """
        <form action="https://formsubmit.co/ramchandrasunilparab2002@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="Your name" required>
             <input type="email" name="email" placeholder="Your email" required>
             <textarea name="message" placeholder="Your message here"></textarea>
             <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
        # Use Local CSS File
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        local_css("style/style.css")


    if selected == "Admission form":

        castes = ['NT-D', 'NT-C', 'VJ-A', 'SBC', 'SC', 'Open', 'NT-B', 'ST', 'OBC', 'SEBC', 'EBC']

        st.title("Our College Admission Form")

        with st.form("Admission Form",clear_on_submit=True):
            st.write("Step 1")
            with st.expander("Personal Details"):
                first,middle,last = st.columns(3)
                fname = first.text_input("First Name")
                mname = middle.text_input("Middle Name")
                lname = last.text_input("Last Name")

                email,mobile = st.columns(2)
                emailid = email.text_input("Email")
                phone = mobile.text_input("Mobile No.")

                adress = st.text_area("Adress")

                caste = st.selectbox("Cast",castes)

            st.write("Step 2")
            with st.expander("Educational Details"):
                math_marks,total_per,result_id = st.columns(3)
                mmarks = math_marks.number_input("Maths Marks",min_value=35,max_value=100,value=60,step=1)
                percentage = total_per.number_input("Total Percentage",min_value=35,max_value=100,value=56,step=1)
                rid = result_id.text_input("Enter Result id",max_chars=10)

            st.write("Step 3")
            with st.expander("Upload Documents"):
                img1 = st.file_uploader("Upload 12th marksheet")
                caste_img2 = st.file_uploader("Upload caste Certificate")

            selected_subject = st.selectbox("Select Subject for F.Y.B.Sc", ["Bsc-IT", "Bsc(PCM)", "Bsc(PMS)"])
            if st.form_submit_button("Submit"):
                st.balloons()
                st.write("Done!")

# total students applied
# student marks graph