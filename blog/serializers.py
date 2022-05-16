from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Post, Comments, Likes_or_DisLikes, Tag
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.utils import html, model_meta, representation


class CatigoruSerializer(serializers.ModelSerializer):
    """ Сериализатор  категорий """

    class Meta:
        model = Category
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    """ Сеарилизатор выводов постов """

    class Meta:
        model = Post
        fields = ('autor', 'title', 'short_descripthion', 'url', 'image')


class FilterCommentSerializer(serializers.ListSerializer):
    """ Перепреодиление сериализотара, чтобы дочерние комментарии не дублировались """

    def to_representation(self, instance):
        data = instance.filter(parent=None)
        return super().to_representation(data)


class Recursiveparent(serializers.Serializer):
    """ Вложеный сериализаторов дочерних комментариев  """

    def to_representation(self, instance):
        serializer = CommentSerializer(instance)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    """ Сериализатор вывода коментариев """
    autor_comment = serializers.StringRelatedField()
    children = Recursiveparent(many=True)

    class Meta:
        list_serializer_class = FilterCommentSerializer
        model = Comments
        fields = ('autor_comment', 'text', 'children', 'id')


class CommentcreatedSerializer(serializers.ModelSerializer):
    """ Сериализатор добавления комментария """

    class Meta:
        model = Comments
        fields = ('text', 'parent', 'post',)


class Like_Add_Delete_serialisers(serializers.ModelSerializer):
    """ Сериализатор добавления или удаления лайка """

    def update_like(self, validated_data):
        obj, created = Likes_or_DisLikes.objects.update_or_create(
            post=validated_data.get('post', None),
            put=validated_data.get('put', None),
            defaults={'coices_like_dislike': validated_data.get('coices_like_dislike')}
        )
        return obj

    def create(self, validated_data):
        try:
            obj = Likes_or_DisLikes.objects.get(post=validated_data.get('post'), put=validated_data.get('put'))
            if (obj.coices_like_dislike == validated_data.get('coices_like_dislike')):
                print('удалил')
                obj.delete()
                return obj
            else:
                print('изменил')
                return self.update_like(validated_data)
        except ObjectDoesNotExist:
            print('создал')
            return super().create(validated_data)

    class Meta:
        model = Likes_or_DisLikes
        fields = ('coices_like_dislike', 'post')


class LikeViewSerializer(serializers.ModelSerializer):
    """ Сериализатор вывода Лайка """
    put = serializers.StringRelatedField()

    class Meta:
        model = Likes_or_DisLikes
        fields = ('coices_like_dislike', 'put', 'post')


class PostDetailSerializer(serializers.ModelSerializer):
    autor = serializers.StringRelatedField()
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    tag = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    number_likes = serializers.IntegerField()
    number_dislikes = serializers.IntegerField()
    post_comment = CommentSerializer(many=True)
    post_like_dislike = LikeViewSerializer(many=True)

    class Meta:
        model = Post
        exclude = ['publish']


class PostCreateSerializer(serializers.ModelSerializer):
    """ Сеарилизатор создания поста """


    def create(self, validated_data):
        ModelClass = self.Meta.model
        info = model_meta.get_field_info(ModelClass)
        list_tag = validated_data.pop('tag_list')
        qery_tag = []
        for tag in list_tag:
            qery_tag.append(Tag.objects.get(name=tag))
        obj = ModelClass.objects.create(**validated_data)
        obj.tag.set(qery_tag)
        return obj

    class Meta:
        model = Post
        fields = ('title', 'short_descripthion', 'descripthion', 'url', 'image', 'publish')


class TagsViewSerializer(serializers.ModelSerializer):
    """ Сеарилизатор вывода всех тегов """

    class Meta:
        model = Tag
        fields = ("id", 'name')
