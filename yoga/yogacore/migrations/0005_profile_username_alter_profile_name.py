# Generated by Django 4.1.13 on 2024-04-08 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yogacore', '0004_rename_username_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='core', max_length=100),
        ),
    ]
