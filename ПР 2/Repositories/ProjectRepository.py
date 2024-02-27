class ProjectRepository:
    def __init__(self):
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def get_projects(self):
        return self.projects

    def add_task_to_project(self, project_id, task):
        project = next((p for p in self.projects if p.id == project_id), None)
        if project:
            project.add_task(task)
