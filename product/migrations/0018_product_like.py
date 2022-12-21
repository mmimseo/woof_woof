# Generated by Django 4.1.1 on 2022-12-18 01:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0017_comment_created_at_comment_modified_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
