# Generated by Django 4.2.5 on 2024-01-30 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0041_a4newpost_alter_a3topfeatured_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='A5NEWPOST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField()),
                ('Text', models.TextField()),
                ('Image', models.ImageField(upload_to='New Post')),
            ],
        ),
    ]
