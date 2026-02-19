class AutonomousAgent:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def make_decision(self):
        if self.tasks:
            # Example decision-making logic
            return self.tasks[0]
        return None

    def execute_task(self, task):
        if task:
            print(f'Executing task: {task}')
            self.tasks.remove(task)

    def run(self):
        while self.tasks:
            task = self.make_decision()
            self.execute_task(task)

# Example usage:
if __name__ == '__main__':
    agent = AutonomousAgent()
    agent.add_task('Task 1')
    agent.add_task('Task 2')
    agent.run()