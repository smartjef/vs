# Generated by Django 4.1.5 on 2023-07-30 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0024_idearequest_refered_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='idearequest',
            options={'ordering': ['-created_at']},
        ),
    ]
