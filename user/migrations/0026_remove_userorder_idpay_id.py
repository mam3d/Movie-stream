# Generated by Django 3.2.9 on 2021-12-20 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_alter_userorder_idpay_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userorder',
            name='idpay_id',
        ),
    ]