# Generated by Django 5.0.6 on 2024-08-24 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0019_order_delivery_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_cost',
        ),
    ]
