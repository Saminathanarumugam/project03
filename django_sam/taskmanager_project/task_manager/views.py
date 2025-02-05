# from django.shortcuts import render

# Create your views here.
# task_manager/views.py
# task_manager/views.py
from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all()  # Fetch all tasks
    return render(request, 'task_manager/task_list.html', {'tasks': tasks})
