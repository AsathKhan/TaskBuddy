# Generated by Django 5.1.2 on 2024-10-28 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BuddyWorks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('customer', 'Customer'), ('staff', 'Staff'), ('manager', 'Manager'), ('admin', 'Admin')], default='customer', max_length=50),
        ),
    ]
