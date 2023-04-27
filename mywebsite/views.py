

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
import uuid
from django.contrib import messages
from .models import Product, Review
from django.core.paginator import Paginator
from django.db.models import Avg

# Create your views here.

def vueapp(request):
    return render(request,"vueapp.html")
    
def home(request):
    resp = render(request, "index.html")
    resp.set_cookie('dev_name','Abdalla')
    return resp


def products(request):
    return render(request, "index.html")


def product_detail(request , slug):
    if request.method == 'POST':
        name = request.POST.get('name')
        rate = request.POST.get('rate')
        review = request.POST.get('review')
     
        data = Review(name=name, review=review, rate=rate)
        data.save()



    product_detail = Product.objects.get(Slug=slug)
    user_review = Review.objects.all()
    num_items = Review.objects.count()

    # Calculate the average rate as a float value
    average_value = Review.objects.aggregate(Avg('rate'))
    average_rate = round(float(average_value['rate__avg']), 1)


    # Define a dictionary of star ratings and their corresponding ranges
    star_ratings = {
        5: range(5, 6),
        4: range(4, 5),
        3: range(3, 4),
        2: range(2, 3),
        1: range(1, 2)
    }

    # Loop through the star ratings dictionary and check the rating value
    # Assign the appropriate star rating if the rating falls within the range
    star_rating = None
    for rating, rating_range in star_ratings.items():
        if int(average_rate) in rating_range:
            star_rating = rating
            break


    # Define Unicode characters for the star shapes and the space character
    filled_star_shape = '\u2605'
    empty_star_shape = '\u2606'
    star_spacing = ' '

    # Create a string of star shapes for the star rating with spaces in between
    stars = (filled_star_shape + star_spacing) * star_rating + (empty_star_shape + star_spacing) * (5 - star_rating)

  
    rate5 = Review.objects.filter(rate = 5.0).count() 
    rate4 = Review.objects.filter(rate = 4.0).count()  
    rate3 = Review.objects.filter(rate = 3.0).count()  
    rate2 = Review.objects.filter(rate = 2.0).count()  
    rate1 = Review.objects.filter(rate = 1.0).count()  

    paginator = Paginator(user_review, 5) # Show 25 contacts per page.
    page= request.GET.get('page')
    user_review  = paginator.get_page(page)   
    context = {
        'product_detail':product_detail,
        'user_review':user_review,
        'num_items':num_items,
        'average_rate':average_rate,
        'stars':stars,
        
        'rate5':rate5,
        'rate4':rate4,
        'rate3':rate3,
        'rate2':rate2,
        'rate1':rate1,
        


        }
    return render(request,'product_detail.html',context)




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

def logout_function(request):
    context = {}
    logout(request)
    return render(request,"index.html",context)

def checkout(request):
    context = {}
    return render(request,"checkout.html",context)