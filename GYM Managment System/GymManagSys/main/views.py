from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from .models import DemoSession
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import LoginRecord
@login_required(login_url='login')
# Home Page...
def home(request):
    return render(request, 'home.html')

def pricing(request):
    return render(request, 'pricing.html')

def success(request):
    return render(request, 'success.html')


def bookDemo(request):
    return render(request, 'bookDemo.html')

def contactUs(request):
    return render(request, 'contactUs.html')


def book_demo(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        preferred_day = request.POST.get('preferred_day')
        preferred_time = request.POST.get('preferred_time')

        form = DemoSession(full_name=full_name,email=email,phone_number=phone_number,preferred_day=preferred_day,preferred_time=preferred_time)
        form.save()
        return render(request,'success.html')

    return render(request,'home.html')

def profile(request):
    return render(request,'profile.html')

def paymentcheckout(request):
    return render(request,'paymentcheckout.html')

def paymentdone(request):
    return render(request,'paymentdone.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
        passwd = request.POST.get('password')
        my_user = User.objects.create_user(fname, lname, email, passwd)
        my_user.save()
        return redirect('login')
    return render(request,'signup.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')  # Get the password from the form
        login_record = authenticate(request, username=username,password=password)
        if login_record is not None:
            login(request,username)
            return redirect('home')
        else:
            return HttpResponse('Username or Password is Incorrect')

    return render(request, 'login.html')


