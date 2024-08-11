from django.shortcuts import render
from .models import Myform

def form(request):
    if request.method =='POST':
        data = request.POST['firstname']
        mylastname = request.POST['lastname']
        my_email = request.POST['email']
        my_password = request.POST['password']
        send = Myform(FirstName=data, LastName=mylastname, MyEmail=my_email, PassWord=my_password )
        send.save()   
    return render(request, 'myform.html', {})
# Create your views here.

# def lastname(request):
#     if request.method =='POST':
#         data = request.POST['lastname']
#         send = Lastname(LastName=data)
#         send.save()
#     return render(request, 'myform.html',)

# def email(request):
#     if request.method =='POST':
#         data = request.POST['email']
#         send = MyEmail(MyEmail=data)
#         send.save()
#     return render(request, 'myform.html',)

# def password(request):
#     if request.method =='POST':
#         data = request.POST['password']
#         send = Mypassword(PassWord=data)
#         send.save()
#     return render(request, 'myform.html',)