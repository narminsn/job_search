# Generated by Django 2.2.6 on 2019-11-12 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Last Name'),
        ),
    ]
