import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state.new_todo = ''

st.title("My Todo App")
st.subheader(" This app can be used to increase your productivity")
st.write("Write your todos:")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        print(todos)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Add new todo", placeholder="Type todo here...", on_change=add_todo, key='new_todo', label_visibility="hidden")
st.session_state