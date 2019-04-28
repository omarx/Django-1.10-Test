from django.contrib.auth import authenticate,login,get_user_model
from django.shortcuts import HttpResponse
from django.shortcuts import render,redirect
from .forms import Contactform,LoginForm,RegisterForm

def home_page(request):
    context={
        "title":"This is the homepage"

    }
    if request.user.is_authenticated():
        context["premium_content"]="Hidden Stuff"
    return render(request,"homepage.html",context)

def contactpage(request):
    contact_form=Contactform(request.POST or None)
    context={
       "title":"Welcome to the Contact Page",
       "forms":contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request,"contact_page.html",context)

def login_page(request):
    form=LoginForm(request.POST or None)
    context={
        "forms":form}
    print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        print(request.user.is_authenticated())
        if user is not None:
            login(request, user)
            #context['form']=LoginForm()
            return redirect("/")
            # Redirect to a success page.
            ...
        else:
            # Return an 'invalid login' error message.
            print("Error")
            ...
    return render(request,"auth/login.html",context)
User=get_user_model()
def register_page(request):
    form=RegisterForm(request.POST or None)
    context={
    "forms":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get('username')
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        new_user=User.objects.create_user(username,email,password)

    return render(request,"auth/register.html",context)
