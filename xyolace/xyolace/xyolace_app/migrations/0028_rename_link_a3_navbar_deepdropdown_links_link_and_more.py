# Generated by Django 4.2.5 on 2024-01-19 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0027_a3_navbar_main_links_alter_a1_top_header_right_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='a3_navbar_deepdropdown_links',
            old_name='link',
            new_name='Link',
        ),
        migrations.RenameField(
            model_name='a3_navbar_deepdropdown_links',
            old_name='title',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='a3_navbar_dropdown_links',
            old_name='link',
            new_name='Link',
        ),
        migrations.RenameField(
            model_name='a3_navbar_dropdown_links',
            old_name='title',
            new_name='Title',
        ),
    ]
