# Generated by Django 4.2.1 on 2023-07-21 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_socialmediaitem_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200, unique=True)),
            ],
        ),
    ]
