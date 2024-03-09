from django.shortcuts import render,redirect
from .models import appModel
from .form import appForm

# Create your views here.

def index(r):
    return render(r,'app/base.html')

def read_operation(r):
    objects=appModel.objects.all()
    my_dict={'objects':objects}
    return render(r,'app/emplist.html',context=my_dict)

def insert_operation(r):
    form=appForm()
    if r.method=="POST":
        form = appForm(r.POST)
        if form.is_valid():
            form.save()
            return redirect("empList")


    return render(r,"app/appform.html",{'form':form})

def update(r,eid):
    emp=appModel.objects.get(eid=eid)
    if r.method=="POST":
        form=appForm(r.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect("empList")
    return render(r,"app/update.html",{'emp':emp})

def delete(r,eid):
    emp=appModel.objects.get(eid=eid)
    emp.delete()
    return redirect("empList")