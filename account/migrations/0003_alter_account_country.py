# Generated by Django 3.2.13 on 2022-07-13 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20220707_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.country'),
        ),
    ]
