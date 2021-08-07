from django.db import models


class Project(models.Model):
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
    add_date = models.DateTimeField('date published', auto_now_add=True)
    is_pub = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=100)
    url = models.CharField(
        max_length=200,
        verbose_name='Ссылка',
        help_text='Ссылка',
    )

    image = models.ImageField(
        upload_to='projects/images/',
        verbose_name='Картинка 370x220',
        null=True,
    )

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title