from django.shortcuts import render
from .models import Category, Image
# Create your views here.


def home(request):
    categories = Category.objects.all()
    images = Image.objects.all()
    context = {'categories': categories, 'images': images}
    return render(request, 'gallery/home.html', context)

def show_image(request, pk):
    return render(request, 'gallery/show_image.html')

def add_image(request):
    return render(request, 'gallery/add_image.html')