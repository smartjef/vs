# Generated by Django 4.1.5 on 2023-08-13 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='unitname',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RemoveField(
            model_name='note',
            name='slug',
        ),
    ]
