# Generated by Django 5.0.1 on 2024-03-09 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_1', models.CharField(max_length=200)),
                ('skill_14', models.CharField(max_length=200)),
                ('skill_15', models.CharField(max_length=200)),
                ('skill_16', models.CharField(max_length=200)),
                ('skill_17', models.CharField(max_length=200)),
                ('skill_18', models.CharField(max_length=200)),
                ('skill_19', models.CharField(max_length=200)),
                ('skill_20', models.CharField(max_length=200)),
                ('skill_21', models.CharField(max_length=200)),
                ('skill_22', models.CharField(max_length=200)),
                ('skill_23', models.CharField(max_length=200)),
                ('skill_24', models.CharField(max_length=200)),
                ('skill_25', models.CharField(max_length=200)),
                ('skill_26', models.CharField(max_length=200)),
            ],
        ),
    ]
