class Task:
    def __init__(self, id, name, description, deadline, responsible, status):
        self.id = id
        self.name = name
        self.description = description
        self.deadline = deadline
        self.responsible = responsible
        self.status = status

    def __eq__(self, other):
        if not isinstance(other, Task):
            return False
        return (self.id, self.name, self.description, self.deadline, self.responsible, self.status) == \
               (other.id, other.name, other.description, other.deadline, other.responsible, other.status)