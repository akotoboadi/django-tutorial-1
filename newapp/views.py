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
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.is_true = True
    feature1.details = 'Our service is very quick'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.is_true = True
    feature2.details = 'Our service is reliable'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Easy to use'
    feature3.is_true = False
    feature3.details = 'Our service is easy to use'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Affordable'
    feature4.is_true =True
    feature4.details = 'Our service is very affordable'

    feature5 = Feature()
    feature5.id = 4
    feature5.name = 'Trustworthy'
    feature5.is_true = True
    feature5.details = 'Our service is filled with trust'

    features = [feature1,feature2,feature3,feature4,feature5]

    
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