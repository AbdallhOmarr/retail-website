

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
import uuid
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, "index.html")


def products(request):
    return render(request, "index.html")


def about(request):
    return render(request, "index.html")


def client(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "index.html")


def login_or_register(request):
    login_form = AuthenticationForm()
    register_form = UserCreationForm()

    if request.method == 'POST':

        form_type = request.POST.get('form_type')

        # Handle login form submission
        if form_type == 'login':
            login_form = AuthenticationForm(data=request.POST)
            if login_form.is_valid():
                print("login is valid")
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    print("user authenticated")
                    login(request, user)
                    return redirect('index')

        # Handle registration form submission
        elif form_type == 'register':
            register_form = UserCreationForm(data=request.POST)
            if register_form.is_valid():
                print("registeration is valid")
                user = register_form.save()
                print("user saved")
                login(request, user)
                print("loged in")
                return redirect('index')
            else:
                print("registeration is not valid")

        elif form_type == 'guest':
            # generate a unique identifier for the guest user
            guest_id = str(uuid.uuid4())
            # store the guest ID in the session
            request.session['guest_id'] = guest_id
            # add a message to inform the user they are shopping as a guest
            messages.info(request, 'You are shopping as a guest. Please provide your information at checkout.')
            # redirect to checkout
            return redirect('index')

        else:
            print("void")
    return render(request, 'login_register.html', {'form': login_form, 'register_form': register_form})

def logout(request):
    context = {}
    return render(request,"login_register.html",context)

def checkout(request):
    context = {}
    return render(request,"checkout.html",context)