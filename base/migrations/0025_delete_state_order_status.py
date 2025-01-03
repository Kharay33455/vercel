# Generated by Django 5.0.6 on 2024-10-20 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_state'),
    ]

    operations = [
        migrations.DeleteModel(
            name='State',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PE', 'Pending'), ('PU', 'Picked up'), ('OH', 'On Hold'), ('OD', 'Out for delivery'), ('IT', 'In-Transit'), ('EN', 'Enroute'), ('CA', 'Cancelled'), ('DE', 'Delivered'), ('RE', 'Returned')], default='PE', max_length=2),
        ),
    ]
