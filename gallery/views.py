from django.shortcuts import render, redirect
from .models import Category, Image
# Create your views here.


def home(request):

    category = request.GET.get('category')
    if category == None:
        images = Image.objects.all()
    else:
        images = Image.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {'categories': categories, 'images': images}
    return render(request, 'gallery/home.html', context)

def show_image(request, pk):
    image = Image.objects.get(id=pk)
    return render(request, 'gallery/show_image.html', {'image': image })

def add_image(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        for image in images:
            image = Image.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('Home')

    context = {'categories': categories}
    return render(request, 'gallery/add_image.html', context)