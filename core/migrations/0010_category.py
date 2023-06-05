# Generated by Django 4.2 on 2023-06-04 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_faq_alter_partner_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=150)),
            ],
        ),
    ]
