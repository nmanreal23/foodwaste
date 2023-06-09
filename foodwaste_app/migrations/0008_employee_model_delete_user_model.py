# Generated by Django 4.2 on 2023-05-20 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodwaste_app', '0007_remove_user_model_id_alter_user_model_firstname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='User_Model',
        ),
    ]
