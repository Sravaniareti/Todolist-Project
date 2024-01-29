from django.shortcuts import render,redirect
from datetime import datetime
from .models import TodoListData



def Todolistdata(request):

    if request.method =='GET':
        data=TodoListData.objects.all()
        return render(request,'Todolist.html',{'data':data})

    else:
        TodoListData(
        title=request.POST.get('title'),
        details=request.POST.get('details'),
        current_time = datetime.now()
        ).save()

        data=TodoListData.objects.all()
        return render(request,'Todolist.html',{'data':data})

def delete_Todolistdata(request,id):
    data=TodoListData.objects.get(id=id)
    data.delete()
    return redirect('Todolistdata')

def update(request,id):
    row=TodoListData.objects.get(id=id)
    return render(request,'update.html',{'row':row})



def updated_data(request,id):
    data=TodoListData.objects.get(id=id)
    data.title=request.POST.get('title')
    data.details=request.POST.get('details')
    data.save()
    return redirect('Todolistdata')









# Create your views here.
