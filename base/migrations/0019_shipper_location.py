# Generated by Django 5.0.6 on 2024-10-16 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_tempuser_first_name_tempuser_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipper',
            name='location',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
