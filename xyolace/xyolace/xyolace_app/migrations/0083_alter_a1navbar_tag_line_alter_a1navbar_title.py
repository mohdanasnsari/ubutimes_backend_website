# Generated by Django 4.2.5 on 2024-02-12 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0082_alter_a1navbar_tag_line_alter_a1navbar_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a1navbar',
            name='Tag_line',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='a1navbar',
            name='Title',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
    ]
