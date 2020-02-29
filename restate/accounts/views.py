from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User


def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #password check
        if (password==password2):

            if User.objects.filter(username=username).exists():
                return HttpResponse("Username already exists")
            
            else:
                if User.objects.filter(email=email).exists():
                    return HttpResponse("Email already exists")

                else:

                    user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,
                    email=email,password=password)
                    user.save()
                    return HttpResponse("U r registered now")




        else :
            return HttpResponse("Passwords Dont Match")

    else:
    
        return render(request,'register.html')

def login(request):

    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            return redirect('login')
   
   
   
    return render(request,'index.html')


def logout(request):

    if request.method=='POST':
        auth.logout(request)


        return redirect('index')


def settings(request):

    cuser=request.user

    context={
        "user":cuser
    }
    return render(request,'settings.html',context)


def delete(request):
    cuser=request.user
    cuser.delete()
    auth.logout()
    return render(request,'index.html')


def pchange(request):
    if request.method =='POST':
        pword=request.POST['password']
        cuser=request.user
        cuser.set_password(pword)
        cuser.save()
    return render(request,'index.html')