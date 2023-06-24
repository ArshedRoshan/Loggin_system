from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def register(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        print('name',Name)
        Email = request.POST['Email']
        Country = request.POST['Country']
        Nationality = request.POST['Nationality']
        Mobile  =  request.POST['Mobile']
        Password = request.POST['Password']
        Roles = request.POST['Roles']
        
        if not Name or not Email or not Country or not Nationality or not Mobile or not Password or not Roles:
            return render(request, 'register.html')
        user = Register.objects.create(Name = Name,Email = Email,Country = Country,Nationality = Nationality,Mobile = Mobile,Password = Password,Roles = Roles)
        print('uu',user)
        if user.Roles == 'student':
            return render(request,'student_login.html')
        if user.Roles == 'admin':
            return render(request,'admin_login.html')
        if user.Roles == 'staff':
            return render(request,'staff_login.html')
        else:
            return render(request,'editor_login.html')
            
    
    return render(request,'register.html')

def student_login(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Password = request.POST['Password']
        
        user = Register.objects.filter(Email=Email,Password = Password).first()
        try:
            user = Register.objects.get(Email=Email, Password=Password)
            if user.Roles == 'student':
                response = render(request, 'home.html', {'user': user})
                response.set_cookie('user', user.Name, httponly=True, samesite='Strict', secure=True)
                response.set_cookie('roles', user.Roles, httponly=True, samesite='Strict', secure=True)
                response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
                return response
            else:
                return render(request, 'student_login.html', {'student': 'You are not a student'})
        except ObjectDoesNotExist:
            return render(request, 'student_login.html', {'message': 'Invalid credentials'})    
    return render(request,'student_login.html')


def staff_login(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Password = request.POST['Password']
        
        user = Register.objects.filter(Email=Email,Password = Password).first()
        print('user',user)
        try:
            if user.Roles == 'staff':
                response = render(request, 'home.html', {'user': user})
                response.set_cookie('user', user.Name, httponly=True, samesite='Strict', secure=True)
                response.set_cookie('roles', user.Roles, httponly=True, samesite='Strict', secure=True)
                response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
                return response
            else:
                return render(request,'staff_login.html',{'staff':'You are not a staff'})
        except ObjectDoesNotExist:
            return render(request,'staff_login.html',{'message':'Invalid credential'})
    return render(request,'staff_login.html')


def admin_login(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Password = request.POST['Password']
        
        user = Register.objects.filter(Email=Email,Password = Password).first()
        print('user',user)
        try:
            if user.Roles == 'admin':
                response = render(request, 'home.html', {'user': user})
                response.set_cookie('user', user.Name, httponly=True, samesite='Strict', secure=True)
                response.set_cookie('roles', user.Roles, httponly=True, samesite='Strict', secure=True)
                response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
                return response
            else:
                return render(request,'admin_login.html',{'admin':'You are not a admin'})
        except ObjectDoesNotExist:
            return render(request,'admin_login.html',{'message':'Invalid credential'})
    return render(request,'admin_login.html')


def editor_login(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Password = request.POST['Password']
        
        user = Register.objects.filter(Email=Email,Password = Password).first()
        print('user',user)
        try:
            if user.Roles == 'editor':
                response = render(request, 'home.html', {'user': user})
                response.set_cookie('user', user.Name, httponly=True, samesite='Strict', secure=True)
                response.set_cookie('roles', user.Roles, httponly=True, samesite='Strict', secure=True)
                response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
                return response
            else:
                return render(request,'editor_login.html',{'editor':'You are not a Editor'})
        except ObjectDoesNotExist:
            return render(request,'editor_login.html',{'message':'Invalid credential'})
    return render(request,'editor_login.html')
    
            
        


def student_logout(request):
    if request.COOKIES['roles'] == 'student':
         response = HttpResponseRedirect('student_login')  # Create a redirect response
    
    if request.COOKIES['roles'] == 'staff':
        response = HttpResponseRedirect('staff_login')
        
    if request.COOKIES['roles'] == 'admin':
        response = HttpResponseRedirect('admin_login')
    
    if request.COOKIES['roles'] == 'editor':
        response = HttpResponseRedirect('editor_login')
    
    response.delete_cookie('user')
    response.delete_cookie('roles')
    
    return response 

# def home(request):
#     print('user' in request.session)
    
    