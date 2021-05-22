from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    """Возвращает посты на главную страницу."""
    latest = Post.objects.all()
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    """Возвращает посты в группе."""
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).all()
    return render(request, "group.html", {"group": group, "posts": posts})
