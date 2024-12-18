from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('post/<int:pk>/',views.post_detail,name='post-detail'),
    path('add/',views.add_post,name='add-post'),
    path('register/',views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('profile/<str:username>/update/', views.profile_update, name='profile-update'), 
]