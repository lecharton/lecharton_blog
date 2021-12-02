from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib.sitemaps.views import sitemap

from blog_sitemap import StaticViewSitemap, PostSitemap, TagSitemap

sitemaps = {
    'index': StaticViewSitemap,
    'posts': PostSitemap,
    'tags': TagSitemap,
}

urlpatterns = [
    path('', include('posts.urls')),
    path('', include('projects.urls')),
    path('', include('about.urls')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)