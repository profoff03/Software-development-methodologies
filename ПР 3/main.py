from lxml import etree
from repositories.RepositoryFactory import get_repository
from models import Project, Task, Responsible, Status, Deadline  # Импортируем необходимые модели
from datetime import date  # Импортируем date из модула datetime


def create_task_element(id, name, description, deadline, responsible, status):
    task = etree.Element('task', id=str(id))
    name_element = etree.SubElement(task, 'name')
    name_element.text = name
    description_element = etree.SubElement(task, 'description')
    description_element.text = description
    deadline_element = etree.SubElement(task, 'deadline')
    deadline_element.text = deadline
    responsible_element = etree.SubElement(task, 'responsible')
    responsible_element.text = responsible
    status_element = etree.SubElement(task, 'status')
    status_element.text = status
    return task


def create_project_element(id, name, description, tasks):
    project = etree.Element('project', id=str(id))
    name_element = etree.SubElement(project, 'name')
    name_element.text = name
    description_element = etree.SubElement(project, 'description')
    description_element.text = description
    tasks_element = etree.SubElement(project, 'tasks')
    for task in tasks:
        tasks_element.append(task)
    return project


def main(repo_type='sql'):
    repository = get_repository(repo_type)

    if repo_type == 'sql':
        from models import Base  # Импортируем Base только в контексте SQL репозитория
        Base.metadata.create_all(bind=repository.session.get_bind())

    # Создаем новую задачу
    responsible = Responsible(id=1, name="John Doe", contact_info="john.doe@example.com")
    status = Status(name="In Progress")
    deadline = Deadline(object_id=1, start_date=date(2024, 5, 1), end_date=date(2024, 6, 1))  # Используем объекты date

    if repo_type == 'sql':
        # Проверяем и добавляем или обновляем Responsible, Status и Deadline
        existing_responsible = repository.session.query(Responsible).filter_by(id=responsible.id).first()
        if not existing_responsible:
            repository.session.add(responsible)

        existing_status = repository.session.query(Status).filter_by(name=status.name).first()
        if not existing_status:
            repository.session.add(status)

        existing_deadline = repository.session.query(Deadline).filter_by(object_id=deadline.object_id).first()
        if not existing_deadline:
            repository.session.add(deadline)

        repository.session.commit()

    new_task = create_task_element(1, "New Task", "Task Description", "2024-06-01", "John Doe",
                                   "In Progress") if repo_type == 'xml' else Task(name="New Task",
                                                                                  description="Task Description",
                                                                                  deadline=deadline,
                                                                                  responsible=responsible,
                                                                                  status=status)

    # Создаем новый проект с задачами
    new_project = create_project_element(1, "New Project", "Project Description",
                                         [new_task]) if repo_type == 'xml' else Project(name="New Project",
                                                                                        description="Project Description",
                                                                                        tasks=[new_task])

    # Добавляем проект в репозиторий
    if repo_type == 'sql':
        repository.session.merge(new_project)  # Используем merge вместо add
        repository.session.commit()
    else:
        repository.add(new_project)

    # Получаем все проекты
    projects = repository.get_all()
    print("Projects:")
    for project in projects:
        if repo_type == 'xml':
            print(etree.tostring(project, pretty_print=True).decode())
        else:
            print(project.name, project.description)

    # Получаем проект по ID
    project_id = '1' if repo_type == 'xml' else new_project.project_id
    project = repository.get_by_id(project_id)
    if project is not None:
        if repo_type == 'xml':
            print("Project by ID 1:", etree.tostring(project, pretty_print=True).decode())
        else:
            print("Project by ID:", project.name, project.description)
            tasks = repository.session.query(Task).filter_by(project_id=project.project_id).all()
            for task in tasks:
                print(task.name, task.description, task.deadline.end_date, task.responsible.name, task.status.name)
    else:
        print(f"Project with ID {project_id} not found")

    # Обновляем проект
    if repo_type == 'xml':
        updated_task = create_task_element(1, "Updated Task", "Updated Description", "2024-06-01", "John Doe",
                                           "Completed")
        updated_project = create_project_element(1, "Updated Project", "Updated Description", [updated_task])
        repository.update(updated_project)
    else:
        project = repository.get_by_id(project_id)
        if project is not None:
            project.description = "Updated Description"
            tasks = repository.session.query(Task).filter_by(project_id=project.project_id).all()
            for task in tasks:
                task.description = "Updated Description"
                task.status.name = "Completed"
            repository.session.commit()
        else:
            print(f"Project with ID {project_id} not found")

    # Получаем обновленный проект по ID
    project = repository.get_by_id(project_id)
    if project is not None:
        if repo_type == 'xml':
            print("Updated Project by ID 1:", etree.tostring(project, pretty_print=True).decode())
        else:
            print("Updated Project by ID:", project.name, project.description)
            tasks = repository.session.query(Task).filter_by(project_id=project.project_id).all()
            for task in tasks:
                print(task.name, task.description, task.deadline.end_date, task.responsible.name, task.status.name)
    else:
        print(f"Project with ID {project_id} not found")

    # Удаляем проект по ID
    repository.delete_by_id(project_id)

    # Проверяем, что проект удален
    projects = repository.get_all()
    print("Projects after deletion:")
    for project in projects:
        if repo_type == 'xml':
            print(etree.tostring(project, pretty_print=True).decode())
        else:
            print(project.name, project.description)
            tasks = repository.session.query(Task).filter_by(project_id=project.project_id).all()
            for task in tasks:
                print(task.name, task.description, task.deadline.end_date, task.responsible.name, task.status.name)


if __name__ == "__main__":
    main(repo_type='xml')  # Change to 'sql' for SQL repository
