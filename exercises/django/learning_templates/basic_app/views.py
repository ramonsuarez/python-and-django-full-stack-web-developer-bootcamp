from django.shortcuts import render


def index(request):
    return render(request, 'basic_app/index.html')

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')
