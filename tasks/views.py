from django.shortcuts import render,redirect,get_object_or_404
from .models import Tasks
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page(request):
    return render(request ,'tasks/homepage.html')

def login_page(request):
    return render(request , 'tasks/login.html')

def signup_page(request):
    return render(request , 'tasks/signup.html')

@login_required
def create_task(request):
    if request.method == 'POST':
        Tasks.objects.create(
            user = request.user,
            name = request.POST.get('name'),
            description = request.POST.get('description'),
            priority = request.POST.get('priority'),
            due_date = request.POST.get('due_date'),
            is_completed=('is_completed' in request.POST),
            status = request.POST.get('status'),
        )
        return redirect('task_list')
    return render(request,'tasks/create_task.html')
@login_required
def update_task(request, id):
    task = get_object_or_404(Tasks, id=id)

    if request.method == 'POST':
        task.name = request.POST.get('name')
        task.description = request.POST.get('description')
        task.priority = request.POST.get('priority')
        task.status = request.POST.get('status')
        task.is_completed = 'is_completed' in request.POST

        due_date = request.POST.get('due_date')
        if due_date:
            task.due_date = due_date
        else:
            task.due_date = None

        task.save()
        return redirect('task_list')

    return render(request, 'tasks/update_task.html', {'task': task})

    
@login_required
def task_list(request):
    tasks = Tasks.objects.filter(user = request.user)
    return render(
        request,
        'tasks/task_list.html',
        {
            'tasks': tasks,
        }
    )
@login_required
def delete_task(request, id):
    task = Tasks.objects.get(id=id)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request, 'tasks/confirm_delete.html', {'task': task})
