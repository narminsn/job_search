# Generated by Django 2.2.6 on 2019-11-09 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompanyApp', '0012_skillsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyvacancy',
            name='skill',
            field=models.ManyToManyField(to='CompanyApp.SkillsModel'),
        ),
    ]
