# Generated by Django 4.2.1 on 2023-07-22 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_aboutusmainsection_aboutusservicesection_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutusteamsection',
            name='twitter_link',
        ),
        migrations.AddField(
            model_name='aboutusteamsection',
            name='linkedin_link',
            field=models.TextField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aboutusteamsection',
            name='behance_link',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='aboutusteamsection',
            name='facebook_link',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='aboutusteamsection',
            name='instagram_link',
            field=models.TextField(max_length=150),
        ),
    ]