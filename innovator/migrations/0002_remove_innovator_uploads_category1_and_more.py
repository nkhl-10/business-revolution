# Generated by Django 4.0.5 on 2023-03-26 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('innovator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='innovator_uploads',
            name='category1',
        ),
        migrations.RemoveField(
            model_name='innovator_uploads',
            name='subcategory1',
        ),
    ]
