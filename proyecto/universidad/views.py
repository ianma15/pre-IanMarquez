from django.shortcuts import render

def index(request):
    return render(request, 'universidad/index.html')
