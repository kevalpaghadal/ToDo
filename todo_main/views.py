from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_complete=False).order_by('-updated_at') #acending and desending order

    complete_task = Task.objects.filter(is_complete=True)

    context = {
        'tasks' : tasks,
        'complete_task' : complete_task 
    }
    return render (request , 'home.html', context)