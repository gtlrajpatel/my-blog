# Generated by Django 2.2.14 on 2020-07-21 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='blog_text',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='blog_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='blog_title',
            new_name='title',
        ),
    ]
