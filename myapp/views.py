from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from .models import Upload_Image
from .forms import IMAGE_UPLOAD

# Create your views here.


def BASE(request):
    return render(request,'include/base.html')
def SIGNUP(request):
    if request.method =="POST":
        un = request.POST.get('username')
        em = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2 :
            return HttpResponse('password2 is incorrect')
        else:
            my_user =User.objects.create_user(un,em,pass1)
            my_user.save()
            return redirect('login/')

    return render(request,'include/signup.html')

def LOGIN(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("upload")
        else:
            return HttpResponse('username or password is incorrect')
    return render(request,'include/login.html')


def UPLOAD_IMAGE(request):
    if request.method == "POST":
        fm = IMAGE_UPLOAD(request.POST, request.FILES)
        if fm.is_valid():
            im = fm.is_valid('image')
            if fm.name.lower().endswith(('.jpg', '.png', '.gif')):
                new_img = UPLOAD_IMAGE(image=im)
                new_img.save()
    else:
        fm = IMAGE_UPLOAD()
    return render(request,'include/upload.html',{'form':fm})


def GALLERY_PAGE(request):
    if request.method == "POST":
        fm = IMAGE_UPLOAD(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = IMAGE_UPLOAD()
    stud = Upload_Image.objects.all()
    return render(request,'include/gallery.html',{'form':fm, 'stu':stud})




