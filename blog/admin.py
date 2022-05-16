from django.contrib import admin
from .models import Category, Tag, Post, Likes_or_DisLikes, Comments

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "description")
    list_display_links = ("name",)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    list_display_links = ("name",)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('autor', 'title', 'short_descripthion', 'descripthion', 'url', 'publish',
                    'date_publish', 'image', 'category')
    list_display_links = ("title",)

@admin.register(Likes_or_DisLikes)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("coices_like_dislike", "post", "put")
    list_display_links = ("post",)


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("autor_comment", "text", 'post', 'parent')
    list_display_links = ("autor_comment",)

