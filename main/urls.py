from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(template_name='main/main.html'), name='main'),
    path('post-create', views.PostCreationView, name='post-create'),
    path('post-delete/<int:pk>/', views.PostDeleteView.as_view(), name='post-delete'),
    path('likes-post', views.LikePostView, name='likes-post'),
    path('weather', views.weatherPageView, name='weather'),



]