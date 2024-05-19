import requests
import streamlit as st

from .utils import url_name, clone_repo


def git_form(repo_path):
    with st.sidebar:
        st.title("Github Link")
        with st.form("git"):
            git_url = st.text_input("Enter GitHub Repository Link")
            submit_git = st.form_submit_button("Submit")
        if submit_git:
            with st.spinner("Checking Github Url"):
                if not (git_url):
                    st.warning("Enter Github Url")
                    st.stop()
                try:
                    response = requests.get(git_url)
                    if response.status_code == 200 and url_name(git_url):
                        st.success("Github Link loaded successfully!")
                        db_name = url_name(git_url)
                    else:
                        st.error("Enter Valid Github Repo")
                        st.stop()
                except requests.exceptions.MissingSchema:
                    st.error(
                        "Invalid Url. Please include the scheme (e.g., http://)")
                    st.stop()

            with st.spinner(f"Cloning {db_name} Repository"):
                clone_repo(git_url, repo_path)
                st.success("Cloned Successfully!")
                return db_name, 1
