# Generated by Django 4.2.5 on 2024-02-04 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0066_rename_text_b3othernews_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='b5trendingtags',
            old_name='Text',
            new_name='Title',
        ),
    ]
