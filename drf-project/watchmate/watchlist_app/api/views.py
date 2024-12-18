from rest_framework.response import Response
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from watchlist_app.models import *
from watchlist_app.api.serializers import *


class ReviewList(generics.ListAPIView):
   # queryset = Review.objects.all()
   serializer_class = ReviewSerializer
   
   def get_queryset(self):
      pk = self.kwargs['pk']
      return Review.objects.filter(watchlist=pk)

class ReviewCreate(generics.CreateAPIView):
   serializer_class = ReviewSerializer
   
   def get_queryset(self):
      return Review.objects.all()
   
   def perform_create(self,serializer):
      pk = self.kwargs.get('pk')
      movie = WatchList.objects.get(pk=pk)
      
      review_user = self.request.user
      review_queryset = Review.objects.filter(watchlist=movie,review_user=review_user)
      
      if review_queryset.exists():
         raise ValidationError("You have already reviewed it")
         
      serializer.save(watchlist=movie,review_user=review_user)
   

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Review.objects.all()
   serializer_class = ReviewSerializer

# class ReviewDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#    queryset = Review.objects.all()
#    serializer_class = ReviewSerializer
#    def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)   
     
#    def put(self, request, *args, **kwargs):
#        return self.update(request, *args, **kwargs)

#    def delete(self, request, *args, **kwargs):
#        return self.destroy(request, *args, **kwargs)

# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class StreamPlatformAV(APIView):
   def get(self,request):
      platform = StreamPlatform.objects.all()
      serializer = StreamPlatformSerializer(platform,many=True)
      return Response(serializer.data)
   
   def post(self,request):
      serializer = StreamPlatformSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      else:
         return Response(serializer.errors)   
      
class StreamDetailAV(APIView):
   def get(self,request,pk):
      try:
         platform = StreamPlatform.objects.get(pk=pk)
      except StreamPlatform.DoesNotExist:
         return Response({'Error':'platform not found'},status=status.HTTP_404_NOT_FOUND)   
      platform = StreamPlatform.objects.get(pk=pk)
      serializer = StreamPlatformSerializer(platform)
      return Response(serializer.data)
   
   def put(self,request,pk):
      platform = StreamPlatform.objects.get(pk=pk)
      serializer = StreamPlatformSerializer(platform,data=request.data)
      
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      else: 
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
   def delete(self,request,pk):
      platform = StreamPlatform.objects.get(pk=pk)
      platform.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)  


class WatchListAV(APIView):
   def get(self,request):
      movies = WatchList.objects.all()
      serializer = WatchListSerializer(movies,many=True)
      return Response(serializer.data )
   
   def post(self,request):
      serializer = WatchListSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      else:
         return Response(serializer.errors)      
   

class WatchDetailAV(APIView):
   def get(self,request,pk):
      try:
         movie = WatchList.objects.get(pk=pk)
      except WatchList.DoesNotExist:
         return Response({'Error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)   
      movie = WatchList.objects.get(pk=pk)
      serializer = WatchListSerializer(movie)
      return Response(serializer.data)
   
   def put(self,request,pk):
      movie = WatchList.objects.get(pk=pk)
      serializer = WatchListSerializer(movie,data=request.data)
      
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      else: 
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
   def delete(self,request,pk):
      movie = WatchList.objects.get(pk=pk)
      movie.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)        



   

# Create your views here.
# @api_view(['GET','POST'])
# def movie_list(request):
#    if request.method == 'GET':
#       movies = Movie.objects.all()
#       serializer = MovieSerializer(movies,many=True)
#       return Response(serializer.data )
#    if request.method == 'POST':
#       serializer = MovieSerializer(data=request.data)
#       if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data)
#       else:
#          return Response(serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
#    if request.method == 'GET': 
#       try:
#          movie = Movie.objects.get(pk=pk)
#       except Movie.DoesNotExist:
#          return Response({'Error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)   
#       movie = Movie.objects.get(pk=pk)
#       serializer = MovieSerializer(movie)
#       return Response(serializer.data)
   
#    if request.method == 'PUT':
#       movie = Movie.objects.get(pk=pk)
#       serializer = MovieSerializer(movie,data=request.data)
      
#       if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data)
#       else:
#          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
#    if request.method == 'DELETE':
#       movie = Movie.objects.get(pk=pk)
#       movie.delete()
#       return Response(status=status.HTTP_204_NO_CONTENT)      