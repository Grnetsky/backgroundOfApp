# Generated by Django 3.2.8 on 2021-11-06 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_user_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='head_portrait',
            field=models.ImageField(default='media/head_portrait/头像.jpg', upload_to='head_portrait', verbose_name='头像'),
        ),
    ]
