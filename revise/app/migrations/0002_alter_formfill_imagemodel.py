# Generated by Django 5.1.6 on 2025-02-28 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfill',
            name='imagemodel',
            field=models.FileField(null=True, upload_to='images'),
        ),
    ]
