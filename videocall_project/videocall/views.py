from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html', {'success': 'you successfully signup.! Please Login.! '})
        else:
            error_message = form.error_messages.text()
            return render(request, 'register.html', {'error': error_message})

    return render(request, 'register.html', {})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials, Please Try Again.! '})

    return render(request, 'login.html', {})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'name': request.user.first_name})


@login_required
def videocall(request):
    return render(request, 'videocall.html', {'name': request.user.first_name + " " + request.user.last_name})


@login_required
def logout_view(request):
    login(request, user=request.user)
    return redirect('login')


@login_required
def join_meeting(request):
    return render(request, 'join_meeting.html', {})

