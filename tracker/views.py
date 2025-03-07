from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tasks, TeamMember
from .forms import TaskForm


@login_required
def dashboard(request):
    tasks = Tasks.objects.all()
    return render(request, 'tracker/dashboard.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'tracker/add_task.html', {'form': form})

@login_required
def update_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tracker/update_task.html', {'form': form})
