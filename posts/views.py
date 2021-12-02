from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Post, Tag
from projects.models import Project

# @cache_page(20, key_prefix='index_page')
def index(request):
    post_list = Post.objects.all()[:4]
    projects = Project.objects.all()[:4]

    return render(
        request,
        'index.html',
        {
            'post_list': post_list,
            'project_list': projects
        }
    )

def blog(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(
        request,
        'blog.html',
        {
            'page': page,
            'main_title': 'Блог',
            'seo_title': 'Блог девушки-программистки',
            'seo_description': 'Блог о программировании: IT новости, советы новичкам, туториалы по Python и немного простой программерской жизни.',
        }
    )


def posts_by_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)

    post_list = tag.posts.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(
        request,
        'blog.html',
        {
            'main_title': tag.title,
            'seo_title': tag.seo_title,
            'seo_description': tag.seo_description,
            'page': page,
        }
    )

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    related_posts = []
    tags = post.tags.all()
    if tags:
        related_posts = tags[0].posts.exclude(pk=post.id)[:2]

    new_posts = Post.objects.exclude(pk=post.id)[:5]

    return render(
        request,
        'post.html',
        {
            'post': post,
            'related_posts': related_posts,
            'new_posts': new_posts
        }
    )