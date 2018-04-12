from django.conf.urls import url
from basic_app import views


app_name = 'basic_app'

urlpatterns = [
        url(r'^$', views.SchoolListView.as_view(), name='list'),
        url(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='detail'),
        url(r'^create/$',views.SchoolCreateView, name='create'),
]
