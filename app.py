import os

import streamlit as st

from components import get_fact_checking, get_paragraphs

PATH_TO_DATA = "data/Promomaterials"


def main():
    st.set_page_config(
        page_title="PDF Document Fact-checking",
        layout="wide",
        initial_sidebar_state="auto",
    )
    st.title("Fact-checking Tool")
    chosen_filename = st.sidebar.selectbox("Choose the file", os.listdir(PATH_TO_DATA))
    _, document_content = get_paragraphs(f"{PATH_TO_DATA}/{chosen_filename}")
    st.subheader("Select paragraphs to fact-check:")
    bool_values = [st.checkbox(par) for par in document_content]
    chosen_paragraphs = [
        item for item, condition in zip(document_content, bool_values) if condition
    ]
    if st.sidebar.button("Start fact-checking:") and chosen_paragraphs:
        result = get_fact_checking(" ".join(chosen_paragraphs))
        st.sidebar.divider()
        st.sidebar.subheader("AI Assistant's comment:")
        st.sidebar.write(result)


if __name__ == "__main__":
    main()
