# Generated by Django 5.0.6 on 2024-06-11 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone_number',
        ),
    ]
