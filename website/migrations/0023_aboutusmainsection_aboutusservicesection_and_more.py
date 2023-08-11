# Generated by Django 4.2.1 on 2023-07-22 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsMainSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='about-us/')),
                ('paragraph_one', models.TextField()),
                ('paragraph_two', models.TextField()),
                ('quote', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AboutUsServiceSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='about-us-service/')),
            ],
        ),
        migrations.CreateModel(
            name='AboutUsTeamSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='about-us-teamMember/')),
                ('facebook_link', models.TextField(max_length=250)),
                ('instagram_link', models.TextField(max_length=250)),
                ('twitter_link', models.TextField(max_length=250)),
                ('behance_link', models.TextField(max_length=250)),
            ],
        ),
    ]