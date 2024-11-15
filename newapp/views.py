from django.shortcuts import render
from django.http import HttpResponse
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