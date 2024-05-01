from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from app.forms import UserForm
# Create your views here.

def signuppage(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully! Login to Continue")
            return redirect('/login')

    return render(request, 'app/user-register.html', {'form' : form})


def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in ")
        return redirect('/home')
    
    else:
        if request.method == "POST":
            u_name = request.POST.get('username')
            passwd = request.POST.get('password')
            
            user = authenticate(request, username = u_name, password =passwd)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect("/home")
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect("/login")
                
                
        return render(request, 'app/user-login.html')
    

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out Successfully ")
        return redirect("/login")
    
    
def home(request):
    # return HttpResponse('Home page')
    return render(request, 'home.html')



