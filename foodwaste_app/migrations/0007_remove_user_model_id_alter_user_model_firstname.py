# Generated by Django 4.2 on 2023-05-20 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodwaste_app', '0006_alter_user_model_firstname_alter_user_model_lastname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_model',
            name='id',
        ),
        migrations.AlterField(
            model_name='user_model',
            name='firstname',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
