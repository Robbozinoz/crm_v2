# project.py

class Project:
    def __init__(self, name, description, customer):
        self.name = name
        self.description = description
        self.customer = customer
        self.tasks = []
        self.team = []
        self.deadline = None

    def display_info(self):
        print(f"Name: {self.name}, Description: {self.description}, Customer: {self.customer}")

    def add_task(self, task):
        self.tasks.append(task)

    def update_progress(self, progress):
        # Placeholder logic: Update project progress
        print(f"Project progress updated to {progress}%")

    def assign_team_member(self, team_member):
        self.team.append(team_member)

    def generate_project_report(self):
        # Placeholder logic: Generate project report
        print("Project report generated")

    def set_deadline(self, deadline):
        self.deadline = deadline
