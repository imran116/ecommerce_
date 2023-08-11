# Generated by Django 4.2.1 on 2023-07-20 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_menu_html_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='html_page',
            field=models.CharField(blank=True, default=False, help_text="Enter the HTML page name without extension (e.g.,'/about' for 'about.html')", max_length=100),
        ),
    ]