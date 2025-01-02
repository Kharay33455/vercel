# Generated by Django 5.0.6 on 2024-06-13 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_id', models.CharField(max_length=10)),
                ('screen_width', models.IntegerField()),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('zoom', models.IntegerField(default=0)),
            ],
        ),
    ]