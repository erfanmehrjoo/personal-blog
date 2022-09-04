from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from blog.models import Post  , Tag
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser , IsAuthenticated , IsAuthenticatedOrReadOnly
from .serializers import PostSerializer , TagSerializer
# Create your views here.
class PostVieSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_fields = ['title' , 'user']
    search_fields = ["title","user__username"]
    ordering_fields = ['created' , 'user']
    ordring = ['-created']


class TagVieSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer





    
