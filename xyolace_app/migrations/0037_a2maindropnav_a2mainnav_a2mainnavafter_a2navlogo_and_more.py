# Generated by Django 4.2.5 on 2024-01-19 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0036_a1topleftnav_a1toprightnav'),
    ]

    operations = [
        migrations.CreateModel(
            name='A2MAINDROPNAV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='A2MAINNAV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30, null=True)),
                ('Link', models.URLField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='A2MAINNAVAFTER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30, null=True)),
                ('Link', models.URLField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='A2NAVLOGO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='Nav Logo')),
            ],
        ),
        migrations.CreateModel(
            name='A2NAVTITLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30, null=True)),
                ('Link', models.URLField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='A2MAINDROPITEMS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Link', models.URLField(default=None)),
                ('dropdown_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deep_dropdown_menus', to='xyolace_app.a2maindropnav')),
            ],
        ),
    ]