# Generated by Django 3.2.4 on 2021-06-08 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0008_auto_20210607_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='created at')),
                ('is_published', models.BooleanField(default=False, verbose_name='Is published?')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Post',
                'db_table': 'post',
            },
        ),
        migrations.AddField(
            model_name='chats',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='url',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='chats',
            name='category',
            field=models.ManyToManyField(blank=True, to='adminapp.Category', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='url',
            name='category',
            field=models.ManyToManyField(blank=True, to='adminapp.Category', verbose_name='Category'),
        ),
    ]