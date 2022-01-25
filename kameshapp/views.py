from django.shortcuts import render,redirect
from .models import kameshmodel
from .forms import kameshform

# Create your views here.
def retrive_view(request):
    model= kameshmodel.objects.all()
    for kamesh in model :
        kamesh.stdrollno +=1
        kamesh.stdmobile +=1
    kameshmodel.objects.bulk_update(model, ['stdrollno','stdmobile'])
    return render(request,"htmlapp/retrive.html",{"model":model})
def insert_view(request) :
    form=kameshform()
    if request.method=="POST" :
        form=kameshform(request.POST)
        if form.is_valid() :
            form.save()
        return redirect("/insert")
    return render(request,"htmlapp/insert.html",{"form":form})

def update_view(request,model_id) :
    model_id = int(model_id)
    try :
        model=kameshmodel.objects.get(id = model_id)
    except kameshmodel.DoesNotExist :
        return redirect("/retrive")
    form = kameshform(request.POST or None, instance = model)
    if form.is_valid() :
        form.save()
        return redirect("/retrive")
    return render(request,"htmlapp/update.html",{"form" :form})

def delete_view(request, model_id) :
    model_id = int(model_id)
    try :
        model=kameshmodel.objects.get(id = model_id)
    except kameshmodel.DoesNotExist :
        return redirect("/retrive")
    model.delete()
    return render(request,"htmlapp/delete.html")

"""def update_view(request,model_id) :
    model=kameshmodel.objects.get(id=id)
    if request.method=="POST" :
        form=kameshform(request.POST,instance=model)
        if form.is_valid() :
            form.save(commit=True)
        return redirect("/retrive")
    return render(request,"htmlapp/update.html",{"model":model})

def delete_view(request,model_id) :
    model = kameshmodel.request.get(id=id)
    if request.method=="GET":
        form=kameshform(request.GET)
        if form.is_valid():
            form.delete(id)
        return redirect("/retrive")"""


