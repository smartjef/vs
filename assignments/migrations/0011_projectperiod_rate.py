# Generated by Django 4.1.5 on 2023-07-30 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0010_period_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectperiod',
            name='rate',
            field=models.FloatField(default=1),
        ),
    ]
