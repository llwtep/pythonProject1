from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('registration', views.registration, name='register'),
    path('login', views.CustomLogin,name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/',views.profileView,name='profile')
]