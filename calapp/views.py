from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def submit(request):
    q = request.GET['query']
    # return HttpResponse(q)
    try:
        ans = eval(q)
        mydict = {
            "q" : q,
            "ans" : ans,
            "error" : "a"
        }
        return render(request,'index.html',context=mydict)
    except:
        mydict = {
            "error" : "b"
        }
        return render(request,'index.html',context=mydict)