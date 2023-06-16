from django.shortcuts import redirect, render
from app.models import Pays,President
from app.forms import PaysForm,PresidentForm,ContinentForm
# Create your views here.


def Continent_create(request):
    if request.method == 'POST':
        form = ContinentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else :
        form = ContinentForm()
    return render (request,"app/create_continent.html",{'form':form})



def President_create(request):
    if request.method == 'POST':
        form = PresidentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else :
        form = PresidentForm()
    return render (request,"app/create_president.html",{'form':form})

def Pays_create(request):
    if request.method == 'POST':
        form = PaysForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = PaysForm()
    return render (request,"app/create_pays.html",{'form':form})


def Home(request):
    pays = Pays.objects.all()
    presidents = President.objects.all()
    context = {
        'pays':pays,
        'presidents':presidents
    }
    return render (request,'app/home.html',context)