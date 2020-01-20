from django.shortcuts import render, redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages

# Create your views here.
def register(request):
  if request.method=='POST':
    first_name=request.POST['First_Name']
    last_name=request.POST['Last_Name']
    email=request.POST['Email']
    user_name=request.POST['User_Name']
    password1=request.POST['password1']
    password2=request.POST['password2']
    if password1!=password2:
      messages.info(request,'password does not match')
      return redirect('register')
    if User.objects.filter(username=user_name).exists():
      messages.info(request,'Username already exists')
      return redirect('register')
    if User.objects.filter(email=email).exists():
      messages.info(request,'Email already exists')
      return redirect('register')
    user = User.objects.create_user(username=user_name, password=password1,email=email, first_name=first_name, last_name=last_name)
    user.save()
    return redirect('/')
    
      
  else:
    return render(request,'register.html')