# Generated by Django 5.0.6 on 2024-09-27 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0023_rename_objectsended_ordercourier_objectsent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderCourier',
        ),
    ]