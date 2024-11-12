from django.urls import path, include
from watchlist_app.api.views import *

urlpatterns = [
    path('list/',WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>',WatchDetailAV.as_view(),name='movie-detail'),
    path('stream/',StreamPlatformAV.as_view(),name='stream'),
    path('stream/<int:pk>',StreamDetailAV.as_view(),name='stream-detail'),
    # path('review/',ReviewList.as_view(),name='review-list'),
    # path('review/<int:pk>',ReviewDetail.as_view(),name='redetail-list')
    path('stream/<int:pk>/review',ReviewList.as_view(),name='review-list'),
    path('stream/<int:pk>/review-create',ReviewCreate.as_view(),name='review-create'),
    path('stream/review/<int:pk>',ReviewDetail.as_view(),name='review-detail'),
]
