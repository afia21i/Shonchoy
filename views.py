from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.shortcuts import render
from .models import *

def webpage(request):
    try:
        webpage = Webpage.objects.all()
    except AttributeError:
        webpage = []
    context = {
        'webpage': webpage,
    }
    return render(request, template_name='pages/webpage.html', context=context)

def homepage(request):
    return render (request,template_name='pages\homepage.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        nid = request.POST.get('nid')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                # Create a new user
                user = User.objects.create_user(username=name, password=password, first_name=name) # Changed username to name
                # Create a MemberProfile
                MemberProfile.objects.create(user=user, phone_number=phone, nid_number=nid)
                login(request, user)  # Log the user in
                return redirect('signupsuccessful')  # Redirect to the success page
            except Exception as e:
                error_message = f"Signup failed: {e}"
                return render(request, 'pages/signup.html', {'error': error_message})
        else:
            error_message = "Passwords do not match."
            return render(request, 'pages/signup.html', {'error': error_message})
    else:
        return render(request, 'pages/signup.html')
    

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
                return render(request, 'pages/login.html', {'form': form})  # Re-render with errors
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'pages/login.html', {'form': form})  # Re-render with errors
    else:
        form = AuthenticationForm(request)
    return render(request, 'pages/login.html', {'form': form})

def signupsuccessful(request):
    return render(request, 'pages/signupsuccessful.html')

def home(request):
    return render (request,template_name='pages\home.html')
def mybank(request):
    return render (request,template_name='pages\mybank.html')
def loaninquiries(request):
    return render (request,template_name='pages\loaninquiries.html')
def chartlist(request):
    return render (request,template_name='pages\chartlist.html')
def currentstatus(request):
    return render (request,template_name='pages\currentstatus.html')
def transactionhistory(request):
    return render(request, template_name='pages/transactionhistory.html')
def myloans(request):
    return render (request,template_name='pages\myloans.html')
def logout(request):
    return render(request, template_name='pages\logout.html')
