from django.shortcuts import render, HttpResponse
# Create your views here.

def index(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse("This is about page.")