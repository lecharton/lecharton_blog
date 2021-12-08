from django.db import models


class Links(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок',
        help_text='Заголовок'
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

    icon = models.CharField(
        max_length=200,
        verbose_name='Имя иконки',
        help_text='Имя иконки',
    )

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title


class AdditionalLinks(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок',
        help_text='Заголовок'
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

    icon = models.CharField(
        max_length=200,
        verbose_name='Имя иконки',
        help_text='Имя иконки',
    )

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title