import streamlit as st
import streamlit_authenticator as stauth

# Not needed but I prefer the aesthetic
st.set_page_config(layout="wide")

# Create the authenticator plugin, and set it to use the auth.yml file
authenticator = stauth.Authenticate("./auth.yml")

# We need to set the authenticator in the session state so it can be accessed in the other pages
st.session_state.authenticator = authenticator

# Single page functions
def login():
    try:
        authenticator.login(callback=lambda x: st.rerun())
    except Exception as e:
        st.error(e)

def logout():
    authenticator.logout("Are you sure?", "sidebar", callback=lambda x: st.rerun())

def register():
    try:
        email, username, name = authenticator.register_user(merge_username_email=True)
        st.success(f"Registered successfully! Your username is {username}")
    except Exception as e:
        st.error(e)

# Main router for different pages
def page():
    login_page = st.Page(login, title="Log in", icon=":material/login:", default=True)
    logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
    register_page = st.Page(register, title="Register", icon=":material/assignment_ind:")

    home_page = st.Page("components/home.py", title="Home", icon=":material/home:", default=True)
    do_something = st.Page("components/do_something.py", title="Do Something", icon=":material/record_voice_over:")

    profile_page = st.Page("components/profile.py", title="Profile", icon=":material/account_circle:")

    # The authenticator plugin stores current authentication status is stored in the session state
    # We set the navigation based on the authentication status
    if st.session_state.authentication_status:
        pg = st.navigation({
            "App": [home_page, do_something],
            "Account": [profile_page, logout_page]
        })
    else:
        pg = st.navigation({
            "Log in": [login_page, register_page]
        })

    pg.run()  

page()