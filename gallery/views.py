from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'gallery/home.html')

def show_image(request, pk):
    return render(request, 'gallery/show_image.html')

def add_image(request):
    return render(request, 'gallery/add_image.html')