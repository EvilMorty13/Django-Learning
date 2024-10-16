from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('post/<int:pk>/',views.post_detail,name='post-detail'),
    path('add/',views.add_post,name='add-post')
]