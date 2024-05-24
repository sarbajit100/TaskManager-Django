from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from taskapp.models import Department, Task
# Create your views here.

def home(request):
    data = {"login":True, "signin":True}
    return render(request,'signin.html', data)


def signin_fun(request):
    if request.method=="POST":
        name = request.POST['txtname']
        email = request.POST['txtemail']
        password = request.POST['txtpswd']
        if User.objects.filter(Q(username=name)|Q(email=email)).exists():
            # data={"msg":True}
            data = {"login":False, "signin":True}
            return render(request,'signin.html',data)
        else:
            u1=User.objects.create_superuser(username=name,email=email,password=password)
            u1.save()
            data = {"login":True, "signin":False}
            return render(request,'signin.html',data)
    {"login":False, "signin":True}
    return render(request,'signin.html', data)

def login_fun(request):
    if request.method=="POST":
        name = request.POST['name']
        password = request.POST['pswd']
        user = authenticate(username=name,password=password)
        if user is not None:
            if user.is_superuser:
                return render(request,'dashboard.html')
            else:
                # data={"msg":True}
                data = {"login":True, "signin":False}
                return render(request,'signin.html',data)
        else:
            data = {"login":True, "signin":False}
            return render(request,'signin.html',data)
    data = {"login":True, "signin":False}
    return render(request,'login.html',data)

def display_fun(request):
    data=Task.objects.all()
    return render(request,'dashboard.html', {"task":data, "display":True})

def add_fun(request):
    department=Department.objects.all()
    if request.method == 'POST':
        t1=Task()
        t1.task_created=request.POST["tskdate"]
        t1.name=request.POST["nametxt"]
        department_id=request.POST.get("dept1")
        department_instance=Department.objects.get(pk=department_id)
        t1.dep=department_instance
        t1.task=request.POST["task"]
        t1.status=request.POST["status"]
        t1.save()
        return redirect('display')
    else:
        return render(request,'dashboard.html', {"display":False, "departments":department, "add":True})
    
def logout_fun(request):
    return redirect('home')


def update_fun(request, id):
    task=Task.objects.get(id=id)
    department=Department.objects.all()
    if request.method=='GET':
        data={"display":False,"task":task, "departments":department, "add":True}
        return render(request, 'dashboard.html', data)
    else:
        data={"display":False,"task":task, "departments":department, "add":True}
        try:
            task.task_created=request.POST["tskdate"]
            task.name=request.POST["nametxt"]
            department_id=request.POST.get("dept1")
            department_instance=Department.objects.get(pk=department_id)
            task.dep=department_instance
            task.task=request.POST["task"]
            task.status=request.POST["status"]
            task.save()
            return redirect('display')
        except:
            return render(request, 'dashboard.html', data)


def delete_fun(request, id):
    task1=Task.objects.get(id=id)
    task1.delete()
    return redirect('display')