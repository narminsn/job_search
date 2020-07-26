from django.db import models

# from CandidateApp.models import CandidatePost
from django.template.defaultfilters import slugify

from base_user.models import MyUser
from django_countries.fields import CountryField
from base_app.models import CategoryModel,  SubcategoryModel
# from CandidateApp.models import CountryModel, CityModel

# from CandidateApp.models import CandidatePost
# Create your models here.
# from CandidateApp.models import CandidatePostImage




class CompanySettings(models.Model):
    stage = (
        ('Startapp', 'Startapp'),
        ('Company', 'Company')
    )

    location = CountryField()
    company_stage = models.CharField(max_length=50, choices=stage)
    phone = models.CharField(max_length=50)
    about = models.TextField()

    def __str__(self):
        return f'{self.location}'


class SkillsModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CompanyVacancy(models.Model):
    category = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Contract', 'Contract'),
        ('Remote', 'Remote')
    )

    seniority_labels = (
        ('Interenship', 'Interenship'),
        ('MidSenior', 'MidSenior'),
    )

    name = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    job_types = models.CharField(max_length=50, choices=category)
    # job_title = models.CharField(max_length=100, choices=seniority_labels)
    job_title = models.CharField(max_length=255)
    job_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    job_sub_category = models.ForeignKey(SubcategoryModel, on_delete=models.CASCADE)
    # location = models.CharField(max_length=100)
    country = models.ForeignKey("CandidateApp.CountryModel", on_delete=models.CASCADE, null=True,blank=True)
    city = models.ForeignKey("CandidateApp.CityModel", on_delete=models.CASCADE,null=True, blank=True)
    city_post = models.CharField(max_length=255, null=True, blank=True)
    # city = models.ForeignKey(CompanyCity, on_delete=models.CASCADE)
    max_salary = models.CharField(max_length=255)
    min_salary = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    starttime = models.CharField(max_length=100, null=True, blank=True)
    endtime = models.CharField(max_length=100, null=True, blank=True)
    job_description = models.TextField()
    image = models.CharField(max_length=255, null=True, blank=True)
    image_post = models.ImageField(upload_to='post', null=True,blank=True)
    create_date = models.DateField(auto_now=True)
    skill = models.ManyToManyField(SkillsModel)
    slug = models.SlugField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.job_title}'

    def get_image(self):
        if self.image_post:
            return self.image_post.url
        else:
            return self.image

    def save(self, *args, **kwargs):
        self.slug = slugify(self.job_title)
        super(CompanyVacancy, self).save(*args, **kwargs)

#
# class VacancySkills(models.Model):
#     vacancy = models.ForeignKey(CompanyVacancy, on_delete=models.CASCADE)
#

#
#
class LikeCompany(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey('CandidateApp.CandidatePost', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

class ApplyCompany(models.Model):
    to_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='company', null=True, blank=True)
    from_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='candidate',null=True,blank=True)
    post = models.ForeignKey(CompanyVacancy, on_delete=models.CASCADE,null=True, blank=True)
    status = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

#
class ApplyCandidate(models.Model):
    to_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='companyy', null=True, blank=True)
    from_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='candidatee',null=True,blank=True)
    post_can = models.ForeignKey('CandidateApp.CandidatePost', on_delete=models.CASCADE,null=True, blank=True)
    status = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class AboutComp(models.Model):
    user  = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    about = models.TextField()
    experience = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.user.username