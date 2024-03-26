class Project:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks
    
    def __eq__(self, other):
        if not isinstance(other, Project):
            return False
        return (self.id, self.name, self.description) == (other.id, other.name, other.description)
