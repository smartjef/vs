# Generated by Django 4.1.5 on 2023-07-26 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0018_remove_payment_idea_payment_idea_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='mpesa_code',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]