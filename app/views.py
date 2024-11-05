from django.shortcuts import render
import os

def index(request):
    img_folder = os.path.join('app', 'static', 'app', 'img')
    iframes = [f for f in os.listdir(img_folder) if f.endswith('.html')]  # or other iframe extensions
    return render(request, 'app/index.html', {'iframes': iframes})