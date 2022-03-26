from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Details
# Create your views here.
def index(request):
    users = Details.objects.all()
    context = {'users':users}
    return render(request,'index.html',context)

def submit(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        detail = Details(name=name,email=email,password=password)
        detail.save()
        return redirect("/")
    return HttpResponse("not valid")

def delete(request,id):
    user = Details.objects.filter(id=id)
    user.delete()
    return redirect('/')


def edit(request,id):
    user = Details.objects.filter(id=id)
    context = {'user':user}
    return render(request,'User.html',context)

def update(request,id):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    context = {name:name,email:email,password:password}
    user = Details.objects.filter(id=id).update(name=name,email=email,password=password)
    # user.save()

    # user.update()
    return redirect('/')