# Generated by Django 4.2.5 on 2024-02-12 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0076_a0pagetop_delete_a0pagelogo_delete_a0pagetitle_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='A1NAVBAR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Image', models.ImageField(default=None, upload_to='Page Logo')),
                ('Nav_links', models.CharField(max_length=30)),
            ],
        ),
    ]
