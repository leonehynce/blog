# Generated by Django 4.2.11 on 2025-02-25 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_blogpost_email_blogpost_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='phone_number',
            field=models.TextField(null=True),
        ),
    ]
