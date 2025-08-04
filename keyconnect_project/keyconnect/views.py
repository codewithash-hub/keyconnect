from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import Loginform

# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = Loginform(request.POST or None)

    if request.method == 'POST':
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            form.add_error(None, 'Invalid username or password.')

    return render(request, 'keyconnect/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')

    
