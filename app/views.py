from django.shortcuts import render

def index(request):
	return render(request, 'app/home.html')

def about(request):
	return render(request, 'app/about.html')
