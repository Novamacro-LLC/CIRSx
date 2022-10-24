# Generated by Django 3.2.13 on 2022-10-21 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_alter_sponsor_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='image',
            field=models.ImageField(default='Transparent-gold.jpg', upload_to='speaker/'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='logo',
            field=models.ImageField(default='Transparent-gold.jpg', upload_to='sponsor/'),
        ),
    ]