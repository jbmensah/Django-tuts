# Generated by Django 5.1 on 2024-08-21 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='is_special',
            field=models.BooleanField(default=False),
        ),
    ]
