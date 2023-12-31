# Generated by Django 4.2.1 on 2023-07-19 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_alter_item_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddCategoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='categoryProducts/')),
                ('title', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='mainbanner',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='is_mainBanner',
        ),
        migrations.AddField(
            model_name='mainbanner',
            name='banner_category_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='addcategoryitem',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.category'),
        ),
    ]
