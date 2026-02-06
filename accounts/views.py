from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login ,authenticate,logout

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request ,'tasks/signup.html',{'error':'User name already Exist'})
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        login(request,user)
        return redirect('task_list')
    return render(request , 'tasks/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return redirect('task_list')
        else:
            return render(request,'tasks/login.html',{'error':'invalid credentials'})
    return render(request,'tasks/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')