from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import SignUpForm


User = get_user_model()


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def homepage(request):
    return render(request, 'homepage.html')

def browse_listings(request):
    #listings = Listing.objects.all()
    #context = {'listings': listings}
    return render(request, 'browse_listings.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'You are now logged in as {username}!')
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')
