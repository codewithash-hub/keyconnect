from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import Loginform, SignupForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = Loginform(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = Loginform()
        
    return render(request, 'keyconnect/login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'keyconnect/home.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password']) # This is hashing the password for protrction
            user.save()
            login(request, user)
            messages.success(request, f"Welcome {user.username}, your account has been created.")
            return redirect('home')
    else:
        form = SignupForm()

    return render(request, 'keyconnect/signup.html')

def logout_user(request):
    logout(request)
    return redirect('login')

    
