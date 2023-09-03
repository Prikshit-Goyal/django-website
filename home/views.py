from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# password = Password@123

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    arr = {
        'variable': "Home"
    }
    return render(request,'home.html',arr)

def about(request):
    if request.user.is_anonymous:
        return redirect("/login")
    arr = {
        'variable': "About"
    }
    return render(request,'about.html',arr)

def services(request):
    if request.user.is_anonymous:
        return redirect("/login")
    arr = {
        'variable': "Services"
    }
    return render(request,'services.html',arr)


def contact(request):
    if request.user.is_anonymous:
        return redirect("/login")
    arr = {
        'variable': "Contact"
    }
    return render(request,'contact.html',arr)

def save_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        contact =  Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        
        messages.success(request, "Form Submitted Successfully.")
        
    arr = {
        'variable': "Contact"
    }
    return render(request,'contact.html',arr)

def loginfunc(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
        
    #     # print(username,password)
    #     user = authenticate(username=username, password=password)

    #     if user is not None:
    #         # A backend authenticated the credentials
    #         login(request, user)
    #         return redirect("/")
    #     else:
    #         # No backend authenticated the credentials
    #         # messages.success(request, "Invalid Login Credentials.")
    #         return render(request,'login.html')

    return render(request,'login.html')

def logoutfunc(request):
    logout(request)
    return render(request,'login.html')

def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # print(username,password)
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            messages.success(request, "Invalid Login Credentials.")
            return render(request,'login.html')
   
## TEXTUTILS  #################################################################################   
def textutils(request):
    arr = {
        'variable': "Home" 
    }
    return render(request,'textutils/home.html',arr)

def result(request):
    text = (request.POST.get('textbox','default'))
    remove_char = request.POST.get('remove_char','off')
    remove_space = request.POST.get('remove_space','off')
    capital = request.POST.get('capital','off')
    char_count = request.POST.get('char_count','off')
    
    analyzed = text
    functionality = ''

    if remove_char == "on":
        characters = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        temp = ""
        functionality = functionality + ' Removed Characters'
        for char in text:
            if char not in characters:
                temp = temp + char
        analyzed = temp
                
    if remove_space == "on":
        temp = ""
        functionality = functionality + ' Removed extra Space'
        for i in range(len(analyzed)-1):
            if analyzed[i]==' ' and analyzed[i+1]==' ':
                pass
            else:
                temp = temp + analyzed[i]
        analyzed = temp
        
    if capital == "on":
        
        analyzed = analyzed.upper()
    
    if char_count == "on":
        analyzed = analyzed
        count = len(analyzed)
        
    # else:
    #     return HttpResponse('Error')
    
    
    params = {
        'purpose': functionality,
        'analyzed_text': analyzed,
        'count' : len(analyzed)
        }
    return render(request, 'textutils/result.html', params)
   
def spaceremove(request):
    # return render(request,'login.html')
    text = (request.POST.get('textbox','default'))
    spaceremove = (request.POST.get('spaceremove','off'))
    
    params = {
        'purpose': "Space removed",
        'analyzed_text': text
    }
    
    return render(request,'textutils/result.html',params)

def capataliizefirst(request):
    return render(request,'login.html')

def charcount(request):
    return render(request,'login.html')
   
## TEXTUTILS  #################################################################################   
