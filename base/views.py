from django.shortcuts import render,redirect
from django.http import HttpResponse , HttpResponseRedirect
from .forms import TaskForm
from .models import Task
import datetime
from django.urls import reverse
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,'frontPage.html')

# tasks = ['Exercise','Home work Shoud be completed today','Computer Repair','Project Completion','E yantra','Flipkart','Leetcode Problems']

def taskPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    st = request.GET.get('st') if request.GET.get('st') != None else 'yet_to_start'
    tasks = Task.objects.filter(
        Q(name__icontains=q) &
        Q(status__iexact=st)
        
    )
    print(request.GET.get('st'))
    print(tasks)
    context = {'tasks':tasks}
    return render(request,'tasks_page.html',context)

def task(request,pk):
    print(pk)
    task = Task.objects.get(id = int(pk))
    context = {'task':task}
    print(task)
    return render(request,'task.html',context)

def addTask(request):
    form = TaskForm()
    # print(form)
    if request.method == 'POST':
        print(request.POST)
        date = request.POST.get('deadlineDate')
        time = request.POST.get('deadlineTime')
        # deadLine = datetime.datetime.strptime(request.POST.get('deadline'), "%Y-%m-%dT%H:%M:%S")
        deadLine = datetime.datetime.strptime(f'{date}T{time}', "%Y-%m-%dT%H:%M")
        
        Task.objects.create(
            name = request.POST.get('name'),
            description = request.POST.get('description'),
            notes = request.POST.get('notes'),
            time = request.POST.get('time'),
            # deadline = request.POST.get('dealine'),
            # score = prioritize(request.POST.get('stress'),)
            deadline = deadLine,
            status = request.POST.get('status'),
            stress = int(request.POST.get('stress')),
        )
        return redirect('tasks')
    context = {'form':form}
    return render(request,'addTask.html',context)

def updateTask(request,pk):
    task = Task.objects.get(id=int(pk))
    form = TaskForm(instance=task)
    dateNow = datetime.datetime.now()
    dateNow = datetime.datetime.strftime(dateNow,'%Y-%m-%d')
    print(dateNow)
    date = datetime.datetime.strftime(task.deadline,'%Y-%m-%d')
    time = datetime.datetime.strftime(task.deadline,'%H:%M')
    if request.method == 'POST':
        print(request.POST)
        date = request.POST.get('deadlineDate')
        time = request.POST.get('deadlineTime')
        # deadLine = datetime.datetime.strptime(request.POST.get('deadline'), "%Y-%m-%dT%H:%M:%S")
        deadLine = datetime.datetime.strptime(f'{date}T{time}', "%Y-%m-%dT%H:%M")
        # print(deadLine2)
        task.name = request.POST.get('name')
        task.description = request.POST.get('description')
        task.notes = request.POST.get('notes')
        task.time = request.POST.get('time')
        # deadline = request.POST.get('dealine'),
        task.deadline = deadLine
        task.status = request.POST.get('status')
        task.stress = int(request.POST.get('stress'))
        print(task)
        task.save()
        context = { 'task' : task }
        return render(request,'task.html',context)
    return render(request,'addTask.html',{'form':form,'date':date,"time":time})

def deleteTask(request,pk):
    task = Task.objects.get(id=int(pk))
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    return render(request,'inform.html',context={'content':f"Are you sure want to delete '{task.name}' ?"})

def completed(request,pk):
    task = Task.objects.get(id=int(pk))
    if request.method == 'POST':
        task.status = 'completed'
        task.save()
        context = {'task':task}
        return render(request,'task.html',context)
        
    return render(request,'inform.html',context={'content':f"Have You Complated '{task.name}' ?"})