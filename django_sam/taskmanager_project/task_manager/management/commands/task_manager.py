# task_manager/management/commands/task_manager.py
from django.core.management.base import BaseCommand
from task_manager.models import Task

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        while True:
            self.stdout.write(
                "Task Manager Menu:\n"
                "1. Add Task\n"
                "2. Edit Task\n"
                "3. Delete Task\n"
                "4. View All Tasks\n"
                "5. Filter Tasks by Priority\n"
                "6. Exit"
            )
            choice = input("Enter your choice: ")

            if choice == '1':
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                priority = input("Enter priority (High/Medium/Low): ")
                status = input("Enter status (Pending/In Progress/Completed): ")
                Task.objects.create(title=title, description=description, priority=priority, status=status)
                self.stdout.write("Task added successfully!")

            elif choice == '2':
                task_id = input("Enter task ID to edit: ")
                task = Task.objects.get(id=task_id)
                title = input(f"Enter new title (current: {task.title}): ") or task.title
                description = input(f"Enter new description (current: {task.description}): ") or task.description
                priority = input(f"Enter new priority (current: {task.priority}): ") or task.priority
                status = input(f"Enter new status (current: {task.status}): ") or task.status
                task.title = title
                task.description = description
                task.priority = priority
                task.status = status
                task.save()
                self.stdout.write("Task edited successfully!")

            elif choice == '3':
                task_id = input("Enter task ID to delete: ")
                task = Task.objects.get(id=task_id)
                task.delete()
                self.stdout.write("Task deleted successfully!")

            elif choice == '4':
                tasks = Task.objects.all()
                for task in tasks:
                    self.stdout.write(str(task))

            elif choice == '5':
                priority = input("Enter priority to filter (High/Medium/Low): ")
                tasks = Task.objects.filter(priority=priority)
                for task in tasks:
                    self.stdout.write(str(task))

            elif choice == '6':
                break

            else:
                self.stdout.write("Invalid choice. Please try again.")
