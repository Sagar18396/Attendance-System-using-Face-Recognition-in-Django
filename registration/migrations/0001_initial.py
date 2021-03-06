# Generated by Django 3.0.6 on 2020-05-26 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('product_key', models.CharField(max_length=100)),
                ('employee_name', models.CharField(max_length=100)),
                ('employee_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('department', models.CharField(max_length=100)),
                ('profile_photo', models.ImageField(upload_to='profile_images/')),
            ],
            options={
                'db_table': 'employee_details',
            },
        ),
        migrations.CreateModel(
            name='ProductKey',
            fields=[
                ('product_key', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Product_Key',
            },
        ),
        migrations.CreateModel(
            name='AdminDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('organisation', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('product_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.ProductKey')),
            ],
            options={
                'db_table': 'Admin_Detail',
            },
        ),
    ]
