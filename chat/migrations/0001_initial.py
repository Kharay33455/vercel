# Generated by Django 5.0.6 on 2024-10-27 17:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pfp', models.ImageField(upload_to='support_pfp')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(max_length=20)),
                ('topic', models.CharField(max_length=200)),
                ('last_message', models.TextField(blank=True, null=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('is_read', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('support', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='chat.support')),
            ],
        ),
        migrations.CreateModel(
            name='ChatUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_new_message', models.BooleanField(default=False)),
                ('pfp', models.ImageField(blank=True, null=True, upload_to='pfp/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='messages')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('from_support', models.BooleanField(default=False)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chat')),
            ],
        ),
    ]
