# Generated by Django 2.2.8 on 2019-12-29 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.STAR_RATINGS_RATING_MODEL),
        ('feedback', '0004_auto_20191229_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='ratings',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.STAR_RATINGS_RATING_MODEL),
        ),
    ]