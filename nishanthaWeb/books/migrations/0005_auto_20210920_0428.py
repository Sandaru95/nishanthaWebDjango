# Generated by Django 3.2.7 on 2021-09-20 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210920_0427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_publisher',
            new_name='publisher',
        ),
    ]