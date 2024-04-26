import base64

from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from .utils import process_image

def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = form.cleaned_data['image']
            filter_type = form.cleaned_data['filter_type']
            kernel_size = form.cleaned_data['kernel_size']

            processed_image_file = process_image(image_file, filter_type, kernel_size)

            if processed_image_file:
                # Encode processed image as base64
                encoded_image = base64.b64encode(processed_image_file.read()).decode('utf-8')
                return HttpResponse(encoded_image)
            else:
                return HttpResponse("Error processing image")
    else:
        form = ImageForm()
    return render(request, 'image_processing/index.html', {'form': form})
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


