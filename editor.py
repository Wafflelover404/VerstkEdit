import streamlit as st

st.title("A Simple Page Editor")
st.markdown("***Edit*** *With* ***Ease***")

uploaded_file = st.file_uploader("Choose your HTML file.")

if uploaded_file is not None:
    bytes_data = uploaded_file.read().decode('utf-8')
    st.write("filename:", uploaded_file.name)
    st.write("Original content:")

    code_editor = st.text_area("Code Editor", value=bytes_data, height=350)
    edited_content = code_editor

    if st.button("Submit"):
        st.header("Page preview")
        st.components.v1.html(code_editor)

    if st.button("Download"):
        st.markdown("### Downloading...")
        st.markdown("please, confirm.")
        st.download_button("Download HTML File", code_editor, uploaded_file.name, "text/html")
else:
    st.write("No file uploaded yet.")
