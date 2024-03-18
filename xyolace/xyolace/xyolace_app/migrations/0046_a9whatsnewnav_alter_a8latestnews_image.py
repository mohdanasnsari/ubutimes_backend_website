# Generated by Django 4.2.5 on 2024-01-30 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0045_a8latestnews'),
    ]

    operations = [
        migrations.CreateModel(
            name='A9WHATSNEWNAV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30, null=True)),
                ('Tab', models.URLField(default=None)),
            ],
        ),
        migrations.AlterField(
            model_name='a8latestnews',
            name='Image',
            field=models.ImageField(upload_to='Latest News'),
        ),
    ]
