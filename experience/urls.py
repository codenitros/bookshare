from django.urls import path , re_path
from . import views

urlpatterns = [
    path('experience/', views.post_list, name='post_list'),
    re_path(r'^experience/(?P<id>\d+)/$', views.detail_view, name='detail'),
]