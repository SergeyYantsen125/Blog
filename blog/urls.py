from django.urls import path

from . import views


urlpatterns = [
    path('category/', views.Category_list.as_view()),
    path('posts/', views.Posts_List.as_view()),
    path('post/created', views.PostCreatedView.as_view()),
    path('post/<str:url>/', views.Post_detail.as_view()),
    path('comment/', views.Comment_create.as_view()),
    path('like/', views.Like_create.as_view()),
    path('tags/', views.TagsAllView.as_view()),

]