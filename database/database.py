import json

class Database:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def get_all_tasks(self):
        return self.tasks

    def get_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None

    def update_task(self, task_id, updated_task):
        for index, task in enumerate(self.tasks):
            if task['id'] == task_id:
                self.tasks[index] = updated_task
                self.save_tasks()
                return True
        return False

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self.save_tasks()

    def get_tasks_by_status(self, status):
        return [task for task in self.tasks if task['status'] == status]

    def get_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task['priority'] == priority]