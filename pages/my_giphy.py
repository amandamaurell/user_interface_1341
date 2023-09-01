import requests
import streamlit as st

url = 'https://api.giphy.com/v1/gifs/random'

tag = st.text_input('Tell me the giphy you would like to see...', value='cat')

params = {
    'api_key':st.secrets.giphy_api_key.API_KEY_2,
    'tag':tag
}

response = requests.get(url, params=params).json()

gif = response['data']['embed_url'] #this is the url of the giphy

st.write(f"<iframe src={gif}>", unsafe_allow_html = True)
