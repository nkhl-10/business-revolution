# Generated by Django 4.1.2 on 2024-10-23 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_rename_aboutus_about_us_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ideas_discription',
            new_name='idea_description',
        ),
        migrations.RenameModel(
            old_name='user_upload',
            new_name='user_upload_idea',
        ),
    ]
