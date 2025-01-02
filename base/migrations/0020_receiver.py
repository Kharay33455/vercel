# Generated by Django 5.0.6 on 2024-10-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_shipper_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address_line', models.TextField()),
                ('address_line2', models.TextField(blank=True, null=True)),
                ('city_and_zip_code', models.TextField()),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]