
from django.urls import path
from .views import PostList,post_detail_view,get_tags,tag_detail_view,post_create_view,delete_post


urlpatterns = [
    path('',PostList.as_view(),name="index"),
    path('create',post_create_view,name="create_post_url"),
    path('post/<str:slug>',post_detail_view,name="post_detail"),
    path('tags',get_tags,name="get_tags"),
    path('tag/<str:slug>',tag_detail_view,name="tag_detail_url"),
    path('delete/<int:pk>',delete_post,name="delete_post")
]
