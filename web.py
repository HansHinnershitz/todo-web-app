import streamlit as st
import functions

todos = functions.read_file()


def add_todo():
    new_todo = st.session_state["new_todo"].title() + "\n"
    todos.append(new_todo)
    functions.write_file(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This will increase your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_file(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="N/A", label_visibility="hidden", placeholder="Add a new item...",
              on_change=add_todo, key="new_todo")
