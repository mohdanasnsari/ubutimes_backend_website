# Generated by Django 4.2.5 on 2024-02-23 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0096_a7ecoandworld_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='A8LIFESTYLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField()),
                ('Text', models.TextField()),
                ('Image', models.ImageField(upload_to='Latest News')),
                ('Source', models.CharField(max_length=40, null=True)),
                ('Time', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
