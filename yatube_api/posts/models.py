from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель Group описывает группы и 
    содержит следующие поля:
    title - название группы (строка, не более 200 символов).
    slug - уникальный идентификатор группы (slug, строка).
    description - описание группы (строка)."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    """Модель Post содержит следующие поля:
    text - текст поста (строка).
    pub_date - дата публикации поста (дата и время, автоматически заполняется при создании поста).
    author - автор поста (связь с моделью User).
    image - изображение поста (опциональное поле для загрузки картинки).
    group - группа, к которой относится пост (связь с моделью Group)."""
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True
    )  # поле для картинки
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE,
        related_name="posts", blank=True, null=True
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Модель Comment описывает комментарии и содержит следующие поля:
    author - автор комментария (связь с моделью User).
    post - пост, к которому относится комментарий (связь с моделью Post).
    text - текст комментария (строка).
    created - дата добавления комментария 
    (дата и время, автоматически заполняется при создании комментария)."""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )
