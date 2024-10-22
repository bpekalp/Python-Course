import streamlit as st
import os
import func.readWrite as rw
import func.dateTimeFormatter as dtf

todos = []
filePath = "data/.todos.txt"
today = str(dtf.formatDateTime())

if not os.path.exists(os.path.dirname(filePath)):
    os.makedirs(os.path.dirname(filePath))

if not os.path.exists("data/.todos.txt"):
    rw.writeTodos(todos, filePath)

todos = rw.readTodos(filePath)

st.title("Coolest To-Do App Ever!")
st.subheader("Arch is the best")
st.text(today)

st.title("My To-Dos")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a To-Do here")
