from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
# Create your views here.

def logoutuser(request):
    logout(request)
    return redirect('homepage')

def loginview(request):
    return render(request,"webera/login.html")

def signupview(request):
    return render(request,"webera/signup.html")

def loginuser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username = username,password = password)
    if user is not None:
        login(request,user)

        return redirect("homepage")
    messages.add_message(request, messages.INFO, 'invalid credentials')
    return redirect(request.META["HTTP_REFERER"])

def registeruser(request):
    username = request.POST["username"]
    password = request.POST["password"]
    repassword = request.POST["repassword"]
    name = request.POST["name"]
    email= request.POST["email"]
    if not User.objects.filter(username = username).exists():
        if password==repassword and len(password)>5 and username.find("01fe18bcs")!=-1 and password.find("@")!=-1  :
            User.objects.create_user(username = username,password=password , first_name= name, email=email).save()
            messages.add_message(request, messages.INFO, 'user succesfully created')
        else:
            messages.add_message(request, messages.INFO, 'Password should contail special charaacter and min 6 characters')
            return redirect(request.META["HTTP_REFERER"])
    else:
        messages.add_message(request, messages.INFO, 'user already exists')
        return redirect(request.META["HTTP_REFERER"])
    # create user

    
    return redirect("loginpage")

def homepageview(request):
    if not request.user.is_authenticated:
        print(request.user)
        return redirect("loginpage")
    context = {
        'user' : request.user,
        'courses' : CourseModel.objects.all()
    }

    if request.user.is_superuser:
        return redirect('/admin/')
    return render(request,"webera/homepage.html",context)

def courseview(request,courseid):
    course = CourseModel.objects.get(id = courseid)
    videos = VideoModel.objects.filter(course = course)
    images = CourseModel.objects.get(id = courseid)
    context = {
        'course' : course,
        'videos' : videos,
        'images' : images
    }
    return render(request,"webera/course.html",context)

def videoview(request,videoid):
    video = VideoModel.objects.get(id = videoid)
    images = VideoModel.objects.get(id = videoid)
    context = {
        'video' : video,
        'images':images
    }



    return render(request,"webera/video.html",context)

def about (request):
    return render(request,"webera/about.html")
# def project (request):
#     return render(request,"webera/project.html")


    
