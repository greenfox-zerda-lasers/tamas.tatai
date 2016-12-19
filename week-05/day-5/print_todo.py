# import os

class DisplayTodos:
    def __init__(self):
        self.print_usage = {
        '''
        Python Todo application
        =======================

        Command line arguments:
        -l   Lists all the tasks
        -a   Adds a new task
        -r   Removes a task
        -c   Completes a task
        '''
        }

    # def display(self):
    #     os.system('cls' if os.name == 'nt' else 'clear')
    #     print (self.usage)

    def print_this(self, data):
        for x, value in enumerate(data,start=1):
            print(str(x), value.rstrip())
