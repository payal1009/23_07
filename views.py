from django.shortcuts import render, HttpResponse
from .models import modelClass
def index(request):
    return render(request,"index.html")

def register(request):
    x = modelClass.objects.all()
    if request.method == 'POST':
        i=request.POST['quantity']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['pwd']
        y = request.POST.get('email')
        events = modelClass.objects.filter(email=y)
        if events.exists():
            return HttpResponse("Account exist")
        else:
            new_event = modelClass(i=i,name=name, email=email, ph=phone, password=password)
            new_event.save()
            return HttpResponse("Account Created")
    return render(request, 'page1.html')

def delete(request):
    if request.method == 'POST':
        event_id = request.POST.get('email')
        events = modelClass.objects.filter(email=event_id)
        if events.exists():
            events.delete()
            return HttpResponse("Account deleted")
        else:
            return HttpResponse("Account not exist")
    return render(request, 'page2.html')  

def update(request):
    if request.method == 'POST':
        event_id = request.POST.get('pwd')
        events = modelClass.objects.filter(password=event_id)
        if events.email==events:
            email=request.POST['pwd']
            events.save()            
            return HttpResponse("Password Updated")
        else:
            return HttpResponse("Data Not found")
    return render(request, 'page3.html')

def display(request):
    from django.core import serializers
    data = serializers.serialize("python",modelClass.objects.all())
    context={"data":data}
    return render(request,"page4.html",context)

def login(request):
    if request.method=="POST":
        email=request.POST['email']
        pwd=request.POST.get['pwd']
        events = modelClass.objects.filter(password=pwd)
        if events.password !=pwd:
            return HttpResponse("Wrong Password")
        else:
            return HttpResponse("Login")
    return render(request,'page5.html')
  
