from django.contrib.auth.models import User
from django.db import models



class Category(models.Model):
    name = models.CharField('Категория', max_length=20)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=100, unique=True)
    publish = models.BooleanField('Опубликовать категорию', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория поста"
        verbose_name_plural = "Категории постов"

class Tag(models.Model):
    name = models.CharField('Категория', max_length=20)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

class Post(models.Model):
    autor = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    title = models.CharField('Заголовок поста', max_length=50)
    short_descripthion = models.CharField('Краткое описание поста', max_length=200)
    descripthion = models.TextField('Текст поста')
    url = models.SlugField(max_length=100, unique=True)
    publish = models.BooleanField('Опубликовать пост', default=True)
    date_publish = models.DateTimeField('Дата и время создания поста', auto_now=True)
    image = models.ImageField('Фото поста', upload_to="post/", null=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT)
    tag = models.ManyToManyField(Tag, verbose_name='Теги', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Likes_or_DisLikes(models.Model):
    LIKE = 'LK'
    DISLIKE = 'DLK'
    CHOICE_LIKE_DISLIKE = [
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike')
    ]

    coices_like_dislike = models.CharField('Лайк или Дизлайк', choices=CHOICE_LIKE_DISLIKE, max_length=10)
    put = models.ForeignKey(User, verbose_name='Создатель лайка или дизлайка', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост", related_name="post_like_dislike")

    def __str__(self):
        return f'{self.post}-{self.coices_like_dislike}'

    class Meta:
        verbose_name = 'Лайк или дизлайк'
        verbose_name_plural = 'Лайки или Дизлайки'



class Comments(models.Model):
    autor_comment = models.ForeignKey(User, verbose_name='Автор комментария', on_delete=models.CASCADE, null=False)
    text = models.TextField(verbose_name='Текс комментария', null=True)
    post = models.ForeignKey(Post, verbose_name='Пост', on_delete=models.CASCADE, null=True, related_name='post_comment')
    parent = models.ForeignKey('self', verbose_name='Родитель', null=True, on_delete=models.CASCADE, blank=True, related_name='children')

    def __str__(self):
        return f'{self.post}-{self.text}'

    class Meta:
        verbose_name = 'Коментарий поста'
        verbose_name_plural = 'Комментарии поста'





