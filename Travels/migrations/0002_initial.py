# Generated by Django 5.2.3 on 2025-06-14 10:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Travels', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='memoryimage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='travel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='memoryimage',
            name='travel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memory_images', to='Travels.travel'),
        ),
        migrations.AddField(
            model_name='travelimage',
            name='travel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Travels.travel'),
        ),
    ]
