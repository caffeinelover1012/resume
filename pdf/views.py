from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UploadFileForm
# Create your views here.
from .utils import pypdfExtract

def index(request):
    return render(request, 'index.html')

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                text = pypdfExtract(file)[0]
                print("EXTRACTED: ", text)
            except Exception as e:
                print('error', e)
            return render(request, 'success.html', {'text': text})  # Render a success page

    else:
        form = UploadFileForm()
    
    return render(request, 'upload.html', {'form': form})