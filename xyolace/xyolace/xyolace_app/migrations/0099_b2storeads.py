# Generated by Django 4.2.5 on 2024-02-23 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0098_a9bottomnav_b1ouroriginal'),
    ]

    operations = [
        migrations.CreateModel(
            name='B2STOREADS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20)),
                ('Text', models.TextField()),
                ('Image', models.ImageField(upload_to='Ads')),
                ('Button', models.CharField(max_length=20, null=True)),
                ('Link', models.URLField()),
            ],
        ),
    ]
