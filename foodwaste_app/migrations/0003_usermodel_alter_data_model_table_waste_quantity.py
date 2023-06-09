# Generated by Django 4.2 on 2023-05-20 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodwaste_app', '0002_alter_data_model_table_food_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='data_model_table',
            name='waste_quantity',
            field=models.IntegerField(help_text='Weight of food waste in kgs.', max_length=100),
        ),
    ]
