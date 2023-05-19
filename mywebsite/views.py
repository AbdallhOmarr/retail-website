

from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
import uuid
from django.contrib import messages
from .models import Product, Review, Category,SubCategory
from django.core.paginator import Paginator
from django.db.models import Avg
import json
from decimal import Decimal
from django.contrib.auth.decorators import login_required
## this import created error no module django_counties found maybe i need to  install it on my side idk but i commented it for now
# from django_countries.fields import CountryField 
from .forms import CreateUserForm
from django.contrib.auth.models import Group


# Create your views here.

def vueapp(request):
    return render(request,"vueapp.html")


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)
    
def home(request):
    product_list = Product.objects.all()
    average_value = Review.objects.aggregate(Avg('rate'))
    average_rate = round(float(average_value['rate__avg']), 1)
    num_reviews = Review.objects.count()
    categories = Category.objects.all()
    # pro = Product.objects.values('discountprice','price')
    # pro_json = json.dumps(list(pro), cls=DecimalEncoder)
    # pro = Product.objects.values('price', 'discountprice').annotate(discount=(F('price') - F('discountprice')) / F('price') * 100)



    paginator = Paginator(product_list, 20) # Show 25 contacts per page.
    page= request.GET.get('page')
    product_list  = paginator.get_page(page)
    
    context = {
        'product_list':product_list,
        'average_rate':average_rate,
        'num_reviews':num_reviews,
        'categories': categories,
        # 'pro_json':pro_json,
        # 'pro':pro,
        }
    resp = render(request, "index.html",context)
    resp.set_cookie('dev_name','Abdalla')
    return resp




def products(request):
    return render(request, 'index.html')



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

    paginator = Paginator(user_review, 2) # Show 25 contacts per page.
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


def cart(request):
    context = {}
    return render(request,"cart.html",context)

def payment(request):
    context = {}
    return render(request,"payment.html",context)





def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form. is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name = 'customer')
            user.groups.add(group)

            messages.success(request, 'Accounts Was created for ' + username)
            return redirect('accounts:login')

    context = {'form':form}
    return render(request,'register.html',context)




def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username ,password = password )

        if user is not None:
                login(request,user)
                return redirect('accounts:home')
        
        else:
            messages.info(request, 'Username or password is incorrect')


    context = {}
    return render(request,'login.html',context)



# @login_required(login_url='/accounts/login/')
# def profile(request, slug):
#    profile = get_object_or_404(Profile, slug=slug)
#    context = {'profile':profile}
#    return render(request, 'profile.html', context)