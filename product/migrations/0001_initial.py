# Generated by Django 4.2.3 on 2023-12-18 12:58

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('vehicles', 'vehicles'), ('property', 'property'), ('phones', 'phones'), ('electronics', 'electronics'), ('home', 'home'), ('beauty', 'beauty'), ('fashion', 'fashion'), ('sport', 'sport'), ('food', 'food')], max_length=255)),
                ('slug', models.SlugField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_slug', models.SlugField(max_length=255)),
                ('item_description', models.TextField()),
                ('item_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('item_price', models.FloatField()),
                ('item_count', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('item_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='product.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='accounts.merchant')),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
    ]
