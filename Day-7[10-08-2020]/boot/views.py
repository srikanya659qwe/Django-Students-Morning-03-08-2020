from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,'userapp/home.html')

def abts(request):
	return render(request,'userapp/about.html')