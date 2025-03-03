from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Task
from .forms import TaskForm


def check_task_owner(task_owner, request_user):
    if task_owner != request_user:
        raise Http404

@login_required
def index(request):
    """Show all tasks."""
    tasks = Task.objects.filter(owner=request.user).order_by('-published_date')
    context = {'tasks': tasks}
    return render(request, 'task_manager/index.html', context)
 

@login_required
def update_status(request, task_id):
    """Update the status of a task (Completed or Not Completed)."""
    task = get_object_or_404(Task, id=task_id)

    # Toggle task status
    task.status = not task.status
    task.save()
    return redirect('task_manager:index')


@login_required
def new_task(request):
    """Create new tasks."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TaskForm()
    else:
        # POST data submitted; process data.
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            return redirect('task_manager:index')
    
    context = {'form': form}
    return render(request, 'task_manager/new_task.html', context)


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    check_task_owner(task.owner, request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('task_manager:index')
    
    context = {'task': task}
    return render(request, 'task_manager/delete_task.html', context)


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    check_task_owner(task.owner, request.user)

    if request.method != 'POST':
        # GET request; show a filled form  
        form = TaskForm(instance=task)
    else:
        # POST request; update the form
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('task_manager:index')
    
    context = {'form': form, 'task': task}
    return render(request, 'task_manager/edit_task.html', context)