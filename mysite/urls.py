from django.urls import path
from . import views

urlpatterns = [
    path('', views.journal_list, name='journal_list'),
    path(r'^journal/(?P<pk>[0-9]+)/$', views.journal_detail, name='journal_detail'),
]
