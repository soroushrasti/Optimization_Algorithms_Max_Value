from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

costs=[
        {"k":3,"naive":"254 micro second",'efficient':"206 micro second"},
        {"k":7,"naive":"147 millisecond",'efficient':"1 millisecond"},
        {"k":12,"naive":"7 minutes",'efficient':"2 millisecond"},
    ]
def index(request):
    return render(request, "optimization/index.html", {"costs": costs})
