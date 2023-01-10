from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Image, Comment

# Create your views here.
def home(request):
    context = {}
    return render(request, 'app/home.html', context)

def index(request):
    images = Image.objects.all()
    context = {
        'image_list': images
    }
    return render(request, 'app/index.html', context)

def detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    comments = image.comment_set.all()
    context = {
        'image': image,
        'comments': comments
    }
    return render(request, 'app/detail.html', context)