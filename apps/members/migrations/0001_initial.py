# Generated by Django 5.0.2 on 2024-03-02 12:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='avatars/default.png', upload_to='avatars/', verbose_name='Аватар')),
                ('bio', models.TextField(blank=True, verbose_name='Біографія')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата народження')),
                ('location', models.CharField(blank=True, max_length=255, verbose_name='Місце проживання')),
                ('website', models.URLField(blank=True, verbose_name='Веб-сайт')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Телефон')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
