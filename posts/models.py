from django.db import models
from tinymce.models import HTMLField


class Tag(models.Model):
    title = models.CharField(
        max_length=200, verbose_name='Название', unique=True
    )
    slug = models.SlugField(
        max_length=200, null=True, verbose_name='Слаг', unique=True
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок',
        help_text='Заголовок'
    )
    slug = models.SlugField(
        max_length=200, null=True, verbose_name='Слаг', unique=True
    )
    description = models.TextField(
        verbose_name='Краткое описание',
        help_text='Краткое описание'
    )
    text = models.TextField(
        verbose_name='Текст',
        help_text='Текст'
    )
    add_date = models.DateTimeField('date published', auto_now_add=True)
    is_pub = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')

    tags = models.ManyToManyField(
        Tag,
        related_name='posts',
        verbose_name='Теги',
    )

    image = models.ImageField(
        upload_to='posts/images/',
        verbose_name='Картинка 770x480',
        null=True,
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title