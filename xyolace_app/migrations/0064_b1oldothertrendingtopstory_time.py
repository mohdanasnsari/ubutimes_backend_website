# Generated by Django 4.2.5 on 2024-02-04 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0063_a8latestnews_source_a8latestnews_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='b1oldothertrendingtopstory',
            name='Time',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]