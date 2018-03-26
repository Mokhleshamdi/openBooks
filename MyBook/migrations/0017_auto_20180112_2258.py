# Generated by Django 2.0 on 2018-01-12 22:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MyBook', '0016_auto_20180110_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='copies',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
