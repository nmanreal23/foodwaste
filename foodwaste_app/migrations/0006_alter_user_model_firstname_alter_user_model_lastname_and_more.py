# Generated by Django 4.2 on 2023-05-20 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodwaste_app', '0005_user_model_delete_usermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='firstname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='lastname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
