# Generated by Django 3.2.7 on 2021-09-20 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_remove_book_book_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookAuthor',
        ),
    ]
