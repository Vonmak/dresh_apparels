# Generated by Django 4.2.3 on 2023-12-18 12:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_ordered', models.DateTimeField(blank=True, null=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_ordered', models.BooleanField(default=False)),
                ('shipping_address_line1', models.CharField(max_length=100)),
                ('shipping_address_line2', models.CharField(blank=True, max_length=100, null=True)),
                ('shipping_city', models.CharField(max_length=100)),
                ('shipping_state', models.CharField(max_length=100)),
                ('shipping_zip_code', models.CharField(max_length=10)),
                ('shipping_country', models.CharField(max_length=100)),
                ('items', models.ManyToManyField(to='cart.cartitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='accounts.customer')),
            ],
        ),
    ]
