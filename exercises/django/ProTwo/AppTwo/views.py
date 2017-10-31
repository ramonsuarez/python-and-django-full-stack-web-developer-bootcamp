from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'insert_me' : 'Hello this is views from AppTwo'}
    return render(request,'help/help.html', context=my_dict)
