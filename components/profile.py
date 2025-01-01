import streamlit as st
import streamlit_authenticator as stauth

authenticator = st.session_state.authenticator

st.title(f"Update profile")

try:
    if authenticator.reset_password(st.session_state['username'], key='password'):
        st.success('Password modified successfully')
except Exception as e:
    st.error(e)

st.divider()

try:
    if authenticator.update_user_details(st.session_state['username'], key='details'):
        st.success('Entries updated successfully')
except Exception as e:
    st.error(e)