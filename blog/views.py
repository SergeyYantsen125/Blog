from django.db.models import Count, Q
from django.shortcuts import render

from .models import Category, Post, Tag
from .serializers import CatigoruSerializer, PostDetailSerializer, PostListSerializer, \
    CommentcreatedSerializer, Like_Add_Delete_serialisers, PostCreateSerializer, TagsViewSerializer
from rest_framework import generics, permissions

class Category_list(generics.ListAPIView):
    """ Вывод категорий """
    serializer_class = CatigoruSerializer
    queryset = Category.objects.all()

class Posts_List(generics.ListAPIView):
    """ Вывод списка постов """
    serializer_class = PostListSerializer
    queryset = Post.objects.filter(publish=True)

class Post_detail(generics.RetrieveAPIView):
    """ Вывод детальной информации поста"""
    lookup_field = 'url'
    serializer_class = PostDetailSerializer

    def get_queryset(self):
        queryset = Post.objects.filter(publish=True).\
            annotate(number_likes=Count('post_like_dislike', filter=Q(post_like_dislike__coices_like_dislike='LK'))).\
            annotate(number_dislikes=Count('post_like_dislike', filter=Q(post_like_dislike__coices_like_dislike='DLK')))
        return queryset

class Comment_create(generics.CreateAPIView):
    """ Создание комментария к посту"""
    serializer_class = CommentcreatedSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
       serializer.save(autor_comment=self.request.user)

class Like_create(generics.CreateAPIView):
    """ Создание Лайка к посту"""
    serializer_class = Like_Add_Delete_serialisers
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
       serializer.save(put=self.request.user)

class PostCreatedView(generics.CreateAPIView):
    """ Создание поста"""
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        print((self.request.data.get('tag', None)).split(','))
        serializer.save(autor=self.request.user,
                        category=Category.objects.get(name=self.request.data.get('category', None)),
                        tag_list=self.request.data.get('tag', None).split(','))


class TagsAllView(generics.ListAPIView):
    serializer_class = TagsViewSerializer
    queryset = Tag.objects.all()









