# Generated by Django 4.0.1 on 2022-01-09 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_calendar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]