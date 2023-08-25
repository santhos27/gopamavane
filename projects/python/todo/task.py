class Task:
    def __init__(self, name, completed=False):
        self.name = name
        self.completed = completed

    def complete(self):
        self.completed = True
