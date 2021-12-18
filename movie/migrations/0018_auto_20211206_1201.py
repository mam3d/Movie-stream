# Generated by Django 3.2.9 on 2021-12-06 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0017_alter_rating_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='rating',
            constraint=models.UniqueConstraint(fields=('user', 'movie'), name='movie-user'),
        ),
    ]