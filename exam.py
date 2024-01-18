import json

class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.status = "Нове"

    def change_status(self, new_status):
        self.status = new_status

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, task_dict):
        task = cls(task_dict["title"], task_dict["description"], task_dict["deadline"])
        task.status = task_dict["status"]
        return task

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_tasks_by_status(self, status):
        return [task for task in self.tasks if task.status == status]

    def display_tasks(self):
        print(f"Завдання команди '{self.team_name}':")
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task.title} - Статус: {task.status}")

    def save_to_file(self, filename="team_tasks.json"):
        with open(filename, "w") as file:
            tasks_data = [task.to_dict() for task in self.tasks]
            json.dump({"team_name": self.team_name, "tasks": tasks_data}, file)

    def load_from_file(self, filename="team_tasks.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.team_name = data["team_name"]
                self.tasks = [Task.from_dict(task_data) for task_data in data["tasks"]]
        except FileNotFoundError:
            pass

team = Team("Наша Команда")

task1 = Task("Бек", "Написати Бек", "Виконати до 20.05.2024")
task2 = Task("Конкуренти", "Знайти конкурентів", "Виконати до 18.03.2024")
task3 = Task("Міт", "Провести міт", "Виконати до 23.01.2024")

team.add_task(task1)
team.add_task(task2)
team.add_task(task3)

team.load_from_file()

team.display_tasks()

choice = input("\nВведіть 'додати' або 'змінити': ").lower()

if choice == "додати":
    new_task_title = input("Введіть назву нового завдання: ")
    new_task_description = input("Введіть опис нового завдання: ")
    new_task_deadline = input("Введіть термін виконання нового завдання: ")

    new_task = Task(new_task_title, new_task_description, new_task_deadline)
    team.add_task(new_task)
else:
    task_index = int(input("Введіть номер завдання для зміни статусу: ")) - 1
    selected_task = team.tasks[task_index]

    new_status = input(f"Введіть новий статус для завдання '{selected_task.title}': ")
    selected_task.change_status(new_status)

team.save_to_file()

tasks_in_progress = team.get_tasks_by_status("В процесі")
completed_tasks = team.get_tasks_by_status("Завершене")

print("\nЗавдання в процесі:")
for task in tasks_in_progress:
    print(f"- {task.title}")

print("\nЗавершені завдання:")
for task in completed_tasks:
    print(f"- {task.title}")
