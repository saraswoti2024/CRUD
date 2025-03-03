# Generated by Django 5.1.6 on 2025-02-28 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='formfill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namemodel', models.CharField(max_length=50)),
                ('emailmodel', models.EmailField(max_length=254, unique=True)),
                ('imagemodel', models.ImageField(upload_to='images')),
                ('checkmodel', models.BooleanField(default=False)),
            ],
        ),
    ]
