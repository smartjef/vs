# Generated by Django 4.1.5 on 2023-08-10 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0013_payment_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='period',
            options={'ordering': ['created_at']},
        ),
    ]