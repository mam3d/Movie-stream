# Generated by Django 3.2.9 on 2021-12-05 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20211205_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='actor',
            new_name='actors',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='category',
            new_name='categories',
        ),
    ]