from django.shortcuts import render,HttpResponse
from django.core.files.storage import FileSystemStorage
import os
import shutil
from django.conf import settings
from .models import  User
# Create your views here.

def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        try:
            os.remove(os.path.join(settings.BASE_DIR, 'media/test_file/test_image.jpg'))
        except:
            pass
        myfile = request.FILES['myfile']
        myfile.name = "test_image.jpg"
        fs = FileSystemStorage(location="media/test_file")
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = "/media/test_file/test_image.jpg"
        print(uploaded_file_url)
        return render(request, 'index.html',{'uploaded_file_url':uploaded_file_url})
    return render(request,'index.html')

def registerUser(request):
    if request.method == 'POST' and request.FILES['profile_image']:
        username= request.POST["username"]
        myfile = request.FILES['profile_image']
        myfile.name = username+".jpeg"
        User.objects.create(username=username,profile_pic = myfile)
        return render(request, 'index.html')
    return render(request,'index.html')



def Scan(request):
    if request.method =="POST":
        name_list = []

        unknown_pictures = os.path.join(settings.BASE_DIR,'/media/test_file')
        known_pictures = os.path.join(settings.BASE_DIR, '/media/profile_image')
        command = "face_recognition ."+known_pictures+" ."+unknown_pictures+""
        out = os.popen(command).read()
        each_line = out.split("\n")
        each_line.remove("")
        for l in each_line:
            name = l.split(",")[1]
            name_list.append(name)
        return render(request, 'index.html',{'found':name_list})
    return render(request, 'index.html')
