# Generated by Django 5.0.6 on 2024-06-14 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_order_current_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='expected_date',
            field=models.CharField(default='9-10 Days', max_length=10),
            preserve_default=False,
        ),
    ]