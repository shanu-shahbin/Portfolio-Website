# Generated by Django 5.0.1 on 2024-04-03 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aboutapp', '0005_rename_image_image_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
