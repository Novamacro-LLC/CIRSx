# Generated by Django 3.2.13 on 2022-06-16 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_alter_document_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='author',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='keywords',
            field=models.CharField(max_length=250, null=True),
        ),
    ]