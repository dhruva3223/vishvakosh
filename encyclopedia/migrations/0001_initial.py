# Generated by Django 4.0.6 on 2022-07-09 11:59

from django.db import migrations, models
import encyclopedia.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=encyclopedia.models.get_file_path)),
            ],
        ),
    ]
