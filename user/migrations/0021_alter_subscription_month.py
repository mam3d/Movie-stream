# Generated by Django 3.2.9 on 2021-12-18 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_auto_20211218_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='month',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
