from django.contrib import sitemaps
from django.urls import reverse

from posts.models import Post, Tag


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['index', 'blog', 'projects']

    def location(self, item):
        return reverse(item)


class PostSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Post.objects.filter(is_pub=True)

    def lastmod(self, obj):
        return obj.pub_date


class TagSitemap(sitemaps.Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Tag.objects.all()
