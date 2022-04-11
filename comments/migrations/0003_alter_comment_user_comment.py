# Generated by Django 4.0.3 on 2022-04-06 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0002_alter_comment_comment_alter_comment_date_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]