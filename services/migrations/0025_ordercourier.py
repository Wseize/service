# Generated by Django 5.0.6 on 2024-09-27 07:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0024_delete_ordercourier'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCourier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Received', 'Received'), ('In Progress', 'In Progress'), ('In Transit', 'In Transit'), ('Complete', 'Complete')], default='Received', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('objectSent', models.CharField(max_length=255)),
                ('pickup_address', models.CharField(max_length=255)),
                ('pickup_latitude', models.FloatField()),
                ('pickup_longitude', models.FloatField()),
                ('delivery_address', models.CharField(max_length=255)),
                ('delivery_latitude', models.FloatField()),
                ('delivery_longitude', models.FloatField()),
                ('delivery_time', models.DateTimeField(blank=True, null=True)),
                ('recipient_phone', models.CharField(max_length=20)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
