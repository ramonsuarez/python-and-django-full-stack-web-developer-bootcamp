from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

def index(request):
    return render(request,'home/index.html')

def users(request):
    # All users page
    user_list = User.objects.order_by('first_name')
    user_dict = {'user_list' : user_list}
    return render(request,'users/index.html', context=user_dict)

def user(request):
    pass
    # Help page

def help(request):
    my_dict = {'insert_me' : 'Hello this is views from AppTwo'}
    return render(request,'help/help.html', context=my_dict)