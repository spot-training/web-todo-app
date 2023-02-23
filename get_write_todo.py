FILEPATH = '/Users/beejay/Downloads/D-Workstation/Pythons/StartingPoint/pythonProject/' \
           'streamlit_web_app/web-todo-app/todo_list.txt'


def get_todo(path=FILEPATH):
    """
    Read a text file and return the list of
    to-do items
    """
    with open(path, 'r') as local_file:
        """ Write the to-to items list in the text file """
        local_calendar_display = local_file.readlines()
    return local_calendar_display


def write_todos(to_write, path=FILEPATH):
    with open(path, 'w') as local_file:
        local_file.writelines(to_write)
