import streamlit as st
import os


Sign_up = st.button("Sign up")
login = st.button("Login")
guest_mode = st.button("Guest Mode")

print(f" Sign_up_pressed : {Sign_up}\n Login_pressed : {login}\n guest_mode_pressed : {guest_mode}\n ")


st.title("Super Simple Title")
st.header("This is a header")
st.subheader("Subheader")
st.caption("small text")

st.text("This is fixed-width, plain text. Great for status updates.")
st.write("This is standard text using st.write, which can take almost anything.")

st.markdown("This is standard markdown text.")
st.markdown("**This line is completely bold text.**")
st.markdown("*This line is completely italic text.*")
st.markdown("You can also mix **bold** and *italic* words inside a normal sentence.")

code_example = """
def greet(name):
    print('hello', name)
"""
st.code(code_example, language="python")

st.divider()

st.image(os.path.join(os.getcwd(), "static", "multiple_line plot.png"))
