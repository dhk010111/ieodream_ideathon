# Generated by Django 3.2.5 on 2021-07-04 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='blog',
            new_name='post',
        ),
    ]
