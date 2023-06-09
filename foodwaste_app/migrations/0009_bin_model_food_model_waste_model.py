# Generated by Django 4.2 on 2023-05-20 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodwaste_app', '0008_employee_model_delete_user_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bin_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bin_name', models.CharField(max_length=30)),
                ('Bin_location', models.CharField(max_length=50)),
                ('Bin_capacity', models.IntegerField()),
                ('Bin_status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Food_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fooditem_name', models.CharField(max_length=30)),
                ('fooditem_category', models.CharField(max_length=30)),
                ('fooditem_type', models.CharField(max_length=20)),
                ('fooditem_measurement', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Waste_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waste_quantity', models.IntegerField()),
                ('waste_date', models.DateTimeField()),
                ('waste_reason', models.CharField(max_length=200)),
                ('waste_location', models.CharField(max_length=50)),
                ('waste_disposal_method', models.CharField(max_length=50)),
                ('dollar_amount', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodwaste_app.employee_model')),
                ('food', models.ManyToManyField(to='foodwaste_app.food_model')),
            ],
        ),
    ]
