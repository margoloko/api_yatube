from rest_framework import serializers

from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор PostSerializer содержит следующие поля:
    author - автор поста (slug связь с моделью User).
    text - текст поста.
    pub_date - дата публикации поста.
    image - изображение поста.
    group - группа, к которой относится пост."""
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        model = Post
        fields = ('__all__')
        read_only_fields = ('group',)


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор GroupSerializer содержит следующие поля:
    title - название группы.
    slug - уникальный идентификатор группы.
    description - описание группы."""
    class Meta:
        model = Group
        fields = ('__all__')


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор CommentSerializer содержит следующие поля:
    author - автор комментария (slug связь с моделью User).
    post - пост, к которому относится комментарий.
    text - текст комментария.
    created - дата добавления комментария."""
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        model = Comment
        fields = ('__all__')
        read_only_fields = ('post',)
