from django.shortcuts import render,redirect
from .models import Person
from .forms import PersonForm

# Create your views here.
def homeview(request):

    return render(request,"person_app/home.html",{})
def add_person(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"person_app/add_person.html",{"form":form})

def show(request):
    queryset = Person.objects.all()
    return render(request,"person_app/show.html",{"obj":queryset})

def update_person(request, pk):
    obj = Person.objects.get(pid=pk)
    form = PersonForm(instance=obj)
    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES, instance=obj)

        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"person_app/add_person.html",{"form":form})

def deleteview(request, x):

## directly delete record ##
    # obj = Person.objects.get(pid=x)
    # obj.delete()
    # return redirect("/a1/sv/")

## confirm page ##

    obj = Person.objects.get(pid=x)
    if request.method == "POST":
        obj.delete()
        return redirect("/a1/sv/")
    return render(request,"person_app/success.html",{"obj":obj})