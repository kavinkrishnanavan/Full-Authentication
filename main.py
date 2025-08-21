import streamlit as st

def login_page():
    st.login(provider="google")
    if st.user.is_logged_in:
        # Redirect to home page after successful login by clearing query params
        st.set_query_params()
        st.rerun()

def home_page():
    st.write(f"Hello, {st.user.name}!")
    st.write(f"Email: {st.user.email}")
    if st.button("Logout"):
        st.logout()
        st.rerun()

def main():
    # Use query param 'page' to simulate routing
    query_params = st.get_query_params()
    page = query_params.get("page", ["home"])[0]

    if page == "login":
        login_page()
    else:
        if not st.user.is_logged_in:
            # Redirect to login page if not logged in
            st.set_query_params(page="login")
            st.rerun()
        else:
            home_page()

if __name__ == "__main__":
    main()
