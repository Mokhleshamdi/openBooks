# Generated by Django 2.0 on 2018-01-13 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyBook', '0020_auto_20180113_0226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='content',
        ),
    ]
