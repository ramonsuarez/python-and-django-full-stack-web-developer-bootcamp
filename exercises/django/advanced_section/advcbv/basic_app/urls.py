from django.conf.urls import url
from basic_app import views


app_name = 'basic_app'

urlpatterns = [
        url(r'^$', views.SchoolListView.as_view(), name='list'),
]
