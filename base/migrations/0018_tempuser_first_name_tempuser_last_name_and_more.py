# Generated by Django 5.0.6 on 2024-10-15 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_tempuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempuser',
            name='first_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tempuser',
            name='last_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tempuser',
            name='password',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tempuser',
            name='phone_number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
