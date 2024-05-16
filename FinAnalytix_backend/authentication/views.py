from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login

from .serializers import UserRegistrationSerializer
from .forms import NewUserForm


# Home Page View
def home(request):
    return render(request, template_name='home.html')

# Define a view function for the registration page
def register_user(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
         
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
         
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')
         
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email = email,
            username=username
        )
         
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
         
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/register/')
     
    # Render the registration page template (GET request)
    return render(request, 'register.html')

#Define a View Function that Logs In a User
def login_user(request):
    #Check if the HTTP request method is POST (Form Submission)
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        #Check if user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display Error message if the username does not exist
            messages.error(request, "Invalid Username")
            return redirect('/login/')
    
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
        
        if user is None:
            # Display Error message if the password is incorrect
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log the user in and redirect them to the home page
            login(request, user)
            return redirect('/home/')
    # Render the login page template (GET request)
    return render(request, 'login.html')
