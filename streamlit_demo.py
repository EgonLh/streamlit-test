import streamlit as st;


input_data = st.number_input("Enter a number :");
st.write("The Current number is",input_data);

st.link_button("Go to gallery", "https://example.com/");


st.write("The answer is ",2*(input_data));