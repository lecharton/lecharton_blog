# Generated by Django 3.2.5 on 2021-12-08 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Заголовок', max_length=200, verbose_name='Заголовок')),
                ('description', models.TextField(help_text='Краткое описание', verbose_name='Краткое описание')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('is_pub', models.BooleanField(default=False)),
                ('order', models.PositiveIntegerField(default=100)),
                ('url', models.CharField(help_text='Ссылка', max_length=200, verbose_name='Ссылка')),
                ('icon', models.CharField(help_text='Имя иконки', max_length=200, verbose_name='Имя иконки')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
    ]
