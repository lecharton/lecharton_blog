from django.db import models


class Application(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Имя',
        help_text='Имя'
    )
    surname = models.CharField(
        max_length=200,
        verbose_name='Фамилия',
        help_text='Фамилия',
        null=True,
        blank=True
    )
    description = models.TextField(
        verbose_name='Тест сообщения',
        help_text='Тест сообщения'
    )
    email = models.EmailField(
        max_length=254,
        verbose_name='Email',
        help_text='Email'
    )
    add_date = models.DateTimeField('date published', auto_now_add=True)
    cv_url = models.CharField(
        max_length=200,
        verbose_name='Ссылка',
        help_text='Ссылка',
        null=True,
        blank=True
    )

    TYPE_CHOICES = [
        ('KO', 'Консультация'),
        ('PS', 'Пробное собеседование'),
    ]
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('add_date',)

    def __str__(self):
        return self.name + ' ' + self.surname


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