from django.shortcuts import render
from django.http import HttpResponse

from .models import Image

# Create your views here.

def home(request):
    return render(request, 'app/home.html', {})

def index(request):
    images = Image.objects.all()
    context = {
        'image_list': images,
    }
    return render(request, 'app/index.html', context)
