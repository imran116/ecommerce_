# Generated by Django 4.2.1 on 2023-07-19 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='menu',
            field=models.ForeignKey(limit_choices_to={'is_mainBanner': True}, on_delete=django.db.models.deletion.CASCADE, to='website.menu'),
        ),
    ]