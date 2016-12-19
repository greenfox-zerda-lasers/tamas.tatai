class TodoModel:
    def __init__(self):
        pass

    def read_file(self, bla):
        x = open(bla)
        data = x.readlines()
        return data
