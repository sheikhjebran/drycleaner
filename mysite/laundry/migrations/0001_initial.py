# Generated by Django 4.1.3 on 2022-12-06 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challan_id', models.CharField(max_length=255)),
                ('challan_date', models.DateField()),
                ('delivery_date', models.DateField()),
                ('delivery_type', models.CharField(max_length=20)),
                ('challan_delivery_status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_number', models.CharField(max_length=255)),
                ('customer_address', models.CharField(max_length=255)),
                ('customer_added', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Iteam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracker_status', models.CharField(max_length=20)),
                ('challan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laundry.challan')),
            ],
        ),
        migrations.AddField(
            model_name='challan',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laundry.customer'),
        ),
    ]
