# Generated by Django 4.1.5 on 2023-07-24 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ai', '0012_imagedescription_initial_number_of_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('craeted_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Area Choice',
                'verbose_name_plural': 'Area Choices',
                'ordering': ['-craeted_at'],
            },
        ),
        migrations.CreateModel(
            name='LevelChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('craeted_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Level Choice',
                'verbose_name_plural': 'Level Choices',
                'ordering': ['-craeted_at'],
            },
        ),
        migrations.RenameField(
            model_name='trial',
            old_name='number',
            new_name='image_trial',
        ),
        migrations.AddField(
            model_name='trial',
            name='ideas_trial',
            field=models.IntegerField(default=5),
        ),
        migrations.CreateModel(
            name='IdeaRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idea_requests', to='ai.areachoice')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idea_requests', to='ai.levelchoice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idea_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GeneratedIdeas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=200)),
                ('project_details', models.TextField()),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='generated_ideas', to='ai.idearequest')),
            ],
        ),
    ]