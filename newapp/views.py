from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import Feature

# Create your views here.
def index(request):
    

    
    return render(request,'index.html')
def greet(request,name):

    return render(request,'dynamic.html',{
        "name" : name.capitalize()
    })
# The code above makes a dynamic website that can have a name depending on user 
def greet1 (request):
    name = "Patrick"
    features = Feature.objects.all()
    

   

    

    
    return render(request,'index1.html',{
        "name":name.capitalize(),
        "features": features,
        

        })
# The code above is also dynamic but uses a name from the backend rather than an input from user in ln 8 to ln 12 
def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())

    return render(request,'counter.html',{
        'amount':amount_of_words,

    })
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request,'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username = username).exists():
                messages.info(request,'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save(),
                return redirect('login')
        else:
            messages.info(request,'Password Not The Same')
            return redirect('register')
    else:
        return render(request,'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('login')
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')