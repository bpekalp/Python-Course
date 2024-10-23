import streamlit as st
import os
import func.readWrite as rw
import func.dateTimeFormatter as dtf

todos = []
filePath = "data/.todos.txt"
today = str(dtf.formatDateTime())

if not os.path.exists(os.path.dirname(filePath)):
    os.makedirs(os.path.dirname(filePath))

if not os.path.exists(filePath):
    rw.writeTodos(todos, filePath)

todos = rw.readTodos(filePath)


def addTodo():
    todo = str(st.session_state["tb_Todo"]).strip().title() + "\n"
    todos.append(todo)
    rw.writeTodos(todos, filePath)


st.title("Coolest To-Do App Ever!")
st.subheader("Arch is the best")
st.text(today)

st.title("My To-Dos")

for i, todo in enumerate(todos):
    _key = f"{i}_{todo}"
    checkbox = st.checkbox(todo, key=_key)
    if checkbox:
        todos.pop(i)
        rw.writeTodos(todos, filePath)
        st.rerun()

st.text_input(
    key="tb_Todo",
    on_change=addTodo,
    label="Enter a To-Do here",
    label_visibility="hidden",
    placeholder="Enter a To-Do here",
)

st.session_state
