# Generated by Django 2.2.6 on 2019-11-03 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateCv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_experience', models.IntegerField()),
                ('about', models.TextField()),
                ('location', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('document', models.FileField(upload_to='cv')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CandidatePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('duration_flow', models.CharField(max_length=255)),
                ('budget', models.IntegerField()),
                ('approve_count', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts')),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('work_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.CategoryModel')),
                ('work_subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.SubcategoryModel')),
            ],
        ),
        migrations.CreateModel(
            name='CountryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CandidateApp.CountryModel')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('skill_type', models.CharField(max_length=255)),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CandidateApp.CandidateCv')),
            ],
        ),
        migrations.CreateModel(
            name='CandidatePostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='workerimg')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CandidateApp.CandidatePost')),
            ],
        ),
        migrations.CreateModel(
            name='CandidatePortfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CandidateApp.CandidateCv')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateExpEdu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_type', models.CharField(choices=[('EXP', 'Experience'), ('EDU', 'Education')], default=None, max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('present', models.BooleanField(default=False)),
                ('end_date', models.DateTimeField()),
                ('description', models.TextField()),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CandidateApp.CandidateCv')),
            ],
        ),
    ]
