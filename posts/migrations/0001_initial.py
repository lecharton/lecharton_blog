# Generated by Django 3.2.5 on 2021-08-02 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(help_text='Краткое описание', verbose_name='Краткое описание')),
                ('text', models.TextField(help_text='Текст', verbose_name='Текст')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('is_pub', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
    ]
