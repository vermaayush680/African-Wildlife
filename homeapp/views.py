from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .predictions import check
import os
import paths

# Create your views here.
def home1(request):
    if request.method == 'POST':
        print(request.POST.get("image"))
    return render(request,'index/home1.html')

def home(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(filename)
        predicted = check(filename)
        # print(predicted)
        data = {
            'uploaded_file_url': uploaded_file_url,
            'predicted':predicted,
        }
        print(paths.ROOT_DIR)
        os.chdir(paths.ROOT_DIR)
        return render(request, 'index/predictionfile.html',context=data)
    return render(request,'index/home.html')
