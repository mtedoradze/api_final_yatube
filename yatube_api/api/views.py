from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import filters
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from api.permissions import AuthorOrReadOnly
from api.serializers import (
    PostSerializer,
    CommentSerializer,
    GroupSerializer,
    FollowSerializer
)
from posts.models import Post, Group, Follow

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    """Операции с публикациями."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Операции с комментариями к публикации id=post_id."""
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.select_related('post')

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(post=post, author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Операции с сообществами: только просмотр."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    """
    Операции с подписками:
    просмотр списка своих подписок (с возможностью поиска по автору)
    и создание новой подписки.
    """
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        following = Follow.objects.filter(user=self.request.user)
        return following

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
