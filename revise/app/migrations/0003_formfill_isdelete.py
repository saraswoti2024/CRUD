# Generated by Django 5.1.6 on 2025-03-03 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_formfill_imagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfill',
            name='isdelete',
            field=models.BooleanField(default=False),
        ),
    ]
