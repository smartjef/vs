# Generated by Django 4.1.5 on 2023-08-02 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0012_alter_projectorder_options_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
