import streamlit as st
import get_write_todo

todos = get_write_todo.get_todo()


def add_todo():
    todo = st.session_state['new_todo_input'] + '\n'
    todos.append(todo)
    get_write_todo.write_todos(todos)


st.title('To do App')
st.subheader('This to-do app is to help outline this you plan to do')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        get_write_todo.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

text_input = st.text_input(label='', placeholder='Add a new todo...', on_change=add_todo, key='new_todo_input')


print('Hello Last script')

