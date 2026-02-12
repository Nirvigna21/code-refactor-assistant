import streamlit as st
from analyzer import analyze_code

st.set_page_config(page_title="Code Refactor Assistant")

st.title("🚀 Code Refactor Assistant")
st.write("Paste your Python code below and get refactoring suggestions.")

code_input = st.text_area("Paste Python Code:", height=300)

if st.button("Analyze Code"):
    result = analyze_code(code_input)

    st.subheader("🔍 Issues Found:")
    for issue in result["issues"]:
        st.write("- ", issue)

    st.subheader("💡 Suggestions:")
    for suggestion in result["suggestions"]:
        st.write("- ", suggestion)
