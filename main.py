import streamlit as st

def main():
    st.title("Google Login with st.login")

    # Call login UI - this triggers Google OAuth flow behind the scenes
    st.login("google")

    # After login, user info is accessible via st.user
    if st.user.is_logged_in:
        st.write(f"Hello, {st.user.name}!")
        st.write(f"Your email is {st.user.email}")
        if st.button("Log out"):
            st.logout()
    else:
        st.write("Please log in with Google.")


