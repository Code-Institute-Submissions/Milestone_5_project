# Generated by Django 2.2.8 on 2019-12-29 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_auto_20191229_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='upvotes',
            new_name='upvote',
        ),
    ]
