# Generated by Django 4.1.13 on 2024-04-08 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yogacore', '0002_rename_raa_login_rename_lopa_signup_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(default='core@gmail.com', max_length=254)),
                ('phonenumber', models.CharField(default='9XXXXXXXX', max_length=10)),
                ('idnumber', models.CharField(default='22000XXXXX', max_length=10)),
                ('image', models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8pqpC6IgkvdxOH-qCcentLTmv_U4TeAVMPutepRWn9w&s', max_length=500)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]