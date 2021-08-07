# Generated by Django 3.2.5 on 2021-08-03 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, null=True, unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True, verbose_name='Слаг'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='posts.Tag', verbose_name='Теги'),
        ),
    ]
