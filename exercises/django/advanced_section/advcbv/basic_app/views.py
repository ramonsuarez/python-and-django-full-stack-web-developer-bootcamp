from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Basic injection'
        return context


class SchoolListView(ListView):
    model = models.School


class SchoolDetail(DetailView):
    model = modes.School
    template_name = 'basic_app/school_detail.html'

