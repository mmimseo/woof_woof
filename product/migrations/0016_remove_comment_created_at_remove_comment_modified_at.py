# Generated by Django 4.1.1 on 2022-11-29 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='modified_at',
        ),
    ]
