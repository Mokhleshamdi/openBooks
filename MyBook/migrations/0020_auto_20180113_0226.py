# Generated by Django 2.0 on 2018-01-13 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyBook', '0019_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='text',
        ),
    ]
