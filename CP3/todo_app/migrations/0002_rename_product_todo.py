# Generated by Django 4.1.6 on 2023-02-25 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Todo',
        ),
    ]