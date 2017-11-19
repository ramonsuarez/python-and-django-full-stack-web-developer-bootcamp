from django.shortcuts import render
# from django.http import HttpResponse
# from AppTwo.models import User
from AppTwo.forms import NewUserForm


def index(request):
    return render(request, 'home/index.html')


def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            return('Error: invalid form')

    return render(request, 'users/index.html', {'form': form})


def user(request):
    pass
    # Help page


def help(request):
    my_dict = {'insert_me': 'Hello this is views from AppTwo'}
    return render(request, 'help/help.html', context=my_dict)
