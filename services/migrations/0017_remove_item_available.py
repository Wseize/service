# Generated by Django 5.0.6 on 2024-06-15 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0016_remove_item_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='available',
        ),
    ]