from django.urls import path, re_path
from . import views

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path('', views.index, name='index'),
    path('register/', views.register, name='registration'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='main/index.html'), name='logout'),
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('me/', views.show_profile, name='profile'),
    path('me/delete-account/', views.delete_act, name='delete_acc'),
    path('me/edit-info/', views.edit, name='edit-info'),
    path('me/my-ads/', views.ads, name='ads'),
    re_path(r'^me/my-ads/delete-ad/(?P<pk>\d+)', views.delete_ad, name='delete'),
	re_path(r'^me/my-ads/update-ad/(?P<pk>\d+)', views.update_ad, name='update'),
    path('booksmain/', views.books, name='books'),
    path('booksmain/sem-1', views.sem1, name='sem1'),
    path('sell/', views.sell, name='selling'),
    path('buy/', views.buy, name='buy'),


]
