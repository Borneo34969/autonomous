class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.is_completed = False

    def complete(self):
        self.is_completed = True

    def __str__(self):
        return f'Task(name={self.name}, description={self.description}, is_completed={self.is_completed})'


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.complete()
                break

    def __str__(self):
        return '\n'.join(str(task) for task in self.tasks)