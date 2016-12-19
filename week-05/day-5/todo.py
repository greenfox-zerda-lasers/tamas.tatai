import sys
from print_todo import DisplayTodos
from todo_model import TodoModel

class TodoCtrl:
    def __init__(self):
        self.printtodo = DisplayTodos()
        self.model = TodoModel()
        self.input_list = sys.argv
        self.input_len = len(self.input_list)
        self.input_print_empty()

    def input_print_empty(self):
        print (self.input_list)
        if self.input_len == 1:
            print(self.printtodo.print_usage)
