# Generated by Django 4.1.13 on 2024-03-25 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_feed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='date',
            field=models.DateField(),
        ),
    ]
