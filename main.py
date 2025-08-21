import streamlit as st

client_id = st.secrets["google_client_id"]
redirect_uri = st.secrets["google_redirect_uri"]
scope = "openid email profile"
auth_url = (
    f"https://accounts.google.com/o/oauth2/v2/auth"
    f"?client_id={client_id}"
    f"&redirect_uri={redirect_uri}"
    f"&response_type=code"
    f"&scope={scope}"
    f"&access_type=offline"
)

st.markdown(f"[Login with Google]({auth_url})")
