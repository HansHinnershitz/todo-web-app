FILEPATH = 'todos.txt'

def read_file(filepath=FILEPATH):
    """Read a text file and return the list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_file(todos_arg, filepath=FILEPATH):
    """writes new to-dos items   to the text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


