import streamlit as st


st.title("Google Login with st.login")

if st.user.is_logged_in:
    st.write(f"Hello, {st.user.name}!")
    st.write(f"Your email is {st.user.email}")
    if st.button("Log out"):
        st.logout()
else:
    st.write("Please log in with Google.")
    st.login("google")


