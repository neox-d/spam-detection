# Generated by Django 5.1 on 2024-08-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spamdetection', '0003_alter_myuser_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.CharField(max_length=15, unique=True, verbose_name='phone number'),
        ),
    ]
