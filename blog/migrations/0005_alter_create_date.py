# Generated by Django 5.2.1 on 2025-05-31 07:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_create_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
