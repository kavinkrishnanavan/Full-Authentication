import streamlit as st
import requests
import urllib.parse

# Read credentials from secrets
client_id = st.secrets["google_client_id"]
client_secret = st.secrets["google_client_secret"]
redirect_uri = st.secrets["google_redirect_uri"]
scope = "openid email profile"

# Function to build Google OAuth URL
def build_auth_url():
    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": scope,
        "access_type": "offline",
        "prompt": "consent"
    }
    base_url = "https://accounts.google.com/o/oauth2/v2/auth"
    return f"{base_url}?{urllib.parse.urlencode(params)}"

# Function to exchange code for tokens
def exchange_code(code):
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"
    }
    resp = requests.post(token_url, data=data)
    return resp.json()

# Function to get user info
def get_user_info(access_token):
    userinfo_url = "https://www.googleapis.com/oauth2/v3/userinfo"
    headers = {"Authorization": f"Bearer {access_token}"}
    resp = requests.get(userinfo_url, headers=headers)
    return resp.json()

# Main app logic
def main():
    query_params = st.experimental_get_query_params()
    
    if "code" in query_params:
        code = query_params["code"][0]
        # Exchange code for tokens
        token_response = exchange_code(code)
        
        if "access_token" in token_response:
            user_info = get_user_info(token_response["access_token"])
            
            # Store user info in session_state
            st.session_state["user_info"] = user_info
            
            # Clear the query params manually to avoid reprocessing
            st.experimental_set_query_params()
        else:
            st.error("Failed to get access token.")
    
    if "user_info" in st.session_state:
        st.write(f"Hello, {st.session_state['user_info']['name']}!")
        st.write(f"Email: {st.session_state['user_info']['email']}")
        if st.button("Logout"):
            st.session_state.pop("user_info")
            st.experimental_rerun()
    else:
        auth_url = build_auth_url()
        st.markdown(f"[Login with Google]({auth_url})")

if __name__ == "__main__":
    main()
