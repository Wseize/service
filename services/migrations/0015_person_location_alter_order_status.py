# Generated by Django 5.0.6 on 2024-06-14 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='location',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Received', 'Received'), ('In Progress', 'In Progress'), ('In Transit', 'In Transit'), ('Complete', 'Complete')], default='Received', max_length=20),
        ),
    ]
