# Generated by Django 3.2.13 on 2022-10-14 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_remove_news_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supportpartners',
            name='logo',
        ),
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(null=True, upload_to='news/'),
        ),
    ]
