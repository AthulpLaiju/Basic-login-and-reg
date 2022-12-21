from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth import get_user_model

def signup(request):
    user = get_user_model()
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        if user.objects.filter(email=email).exists():
            messages.info(request,'Email already exists!!')
            return redirect('signup')
        else:
            user = user.objects.create_user(username=username, name=name, email=email,phone=phone,password=password )
            user.save()
            print("User created")
            messages.info(request,'Account created successfully')
            return redirect('login')
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request,username=username, password=password)
        print('USER:',user)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'Logged in successfully')
            return redirect('index')
        else:
            messages.info(request,'Invalid Username or Password!!')
            return redirect('login')

    else:
        return render(request,'login.html')
    

def index(request):
    return render(request,'index.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


