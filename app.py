import streamlit as st
import requests
from bs4 import BeautifulSoup
import re
def display_information(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    st.markdown("## Text Content")
    st.text(re.sub(" ", "",soup.text)[:10])
    st.markdown("## Links in the page:")
    for link in soup.find_all('a')[:10]:
        if link:
            st.markdown("- " + link.get('href'))

    # Get all the tags in the page and display their names
    st.markdown("## Tags in the page:")
    for tag in soup.find_all()[:10]:
        if tag:
            st.markdown("- " + tag.name)
            
    st.markdown("## Images in the page:")
    for img in soup.find_all('img')[:10]:
        if img:
            st.markdown("- " + url+img.get('src'))
    
    # st.markdown("## Meta Data")
    # for meta in soup.find_all('meta')[:10]:
    #     if meta:
    #         st.markdown("- " + meta.get('name') + meta.get('content'))
    
            


st.title("CN Lab Project :- Web Scraper")

url = st.text_input("Enter the URL you want to scrape")

if st.button("Scrape"):
    display_information(url)