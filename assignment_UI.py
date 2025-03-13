import streamlit as st
import time;
def process_Data():
    msg = st.toast("The Data is Processing.....");
    time.sleep(1);
    msg.toast("Denied");

with st.container(border=True):
    col1,col2 = st.columns(2);
    with col1:
        st.write("Gallary")
        username = st.text_input("Enter Username",placeholder="Enter username",max_chars=30);
    with col2:
        st.caption("Welcome ,"+ username);
        options = st.multiselect(
        "Choose Topics",
        ["Topic 1", "Topic 2", "Topic 3", "Topic 4"],
)
col1, col2 = st.columns(2,border=True)

with col1:
    st.caption("Explore Different Topics")
    st.image("https://i.pinimg.com/736x/be/91/78/be91785fa1518c2c081342c5e0346292.jpg")
with col2:
    # Camera Input
    enable = st.checkbox("Enable camera")
    picture = st.camera_input("Take a picture for profile", disabled=not enable)
    if picture:
        st.image(picture)
    if st.button('Fetch Data'):
        process_Data()

with st.container(border=True):
    # Files uploading
    uploaded_files = st.file_uploader(
    "Choose a file for your data", accept_multiple_files=True ,type=["png"], help="Please upload a file"
    )
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)    

