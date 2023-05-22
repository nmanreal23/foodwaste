# Generated by Django 4.2 on 2023-05-20 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodwaste_app', '0004_alter_data_model_table_food_quantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(help_text='name of the user', max_length=30)),
                ('lastname', models.CharField(help_text='surname of the user', max_length=30)),
                ('username', models.CharField(help_text='users preferred username', max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]