# Generated by Django 5.0.1 on 2024-03-12 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='video',
            field=models.FileField(blank=True, upload_to='videos'),
        ),
    ]
