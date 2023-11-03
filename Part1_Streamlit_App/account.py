import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate('fluted-gantry-402510-285695bf6a45.json')
firebase_admin.initialize_app(cred)


def app():

    st.header("**Welcome to :violet[Analytic Platform with End - End Data Pipeline]** :anchor: ")
    st.text('\n')

    # initialize it as empty strings as session state begin when they Log In ~ session state - dict
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''

# V.imp -- use user.uid, user.email fon the next part
    def f(): # Handle the case when we are Logging In
        try:
            user = auth.get_user_by_email(email)
            st.success("Logged in Successfully !")
            st.session_state.username = user.uid
            st.session_state.useremail = user.email

            global Usernm # declared global so as it is accessible to other functions
            Usernm = (user.uid)

            st.session_state.signedout = True
            st.session_state.signout = True


        except: # when email is not correct
            st.warning('Login Failed - Incorrect Email or Password !')

    def t(): # Handle the case when we are signing out from our session
        st.session_state.signout = False
        st.session_state.signedout = False
        st.session_state.username = ''

    if "signedout" not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False

    if not st.session_state["signedout"]:  # only show if the state is False, hence the button has never been clicked
        choice = st.selectbox('Login/Signup', ['Login', 'Sign Up'])
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')

        if choice == 'Sign Up':
            username = st.text_input("Enter your unique username")
            try:
                if st.button('Create my account'):
                    user = auth.create_user(email=email, password=password, uid=username)

                    st.success('Account created successfully!')
                    st.markdown('Please Login using your email and password')
                    st.balloons()
            except (ValueError, TypeError, NameError, AttributeError):
                st.error("Incomplete/ Invalid Email, Username, Password - Please enter Again")
            except:
                st.error("Email or Username Already Exist, Please use another Credentials to Sign Up")

        else: # IF choice is Login
            st.button('Login', on_click=f)

    if st.session_state.signout: # signout is True as we are Logged in
        st.text('User Name ->'+'\t'+ st.session_state.username)
        st.text('Email id ->'+'\t'+st.session_state.useremail)
        st.button('Sign out', on_click=t) # here we change signout & signedout as False after signing out










