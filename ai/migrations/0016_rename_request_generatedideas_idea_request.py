# Generated by Django 4.1.5 on 2023-07-26 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0015_rename_project_details_generatedideas_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generatedideas',
            old_name='request',
            new_name='idea_request',
        ),
    ]