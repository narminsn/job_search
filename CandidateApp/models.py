from django.db import models

# from CompanyApp.models import CompanyVacancy
from django.template.defaultfilters import slugify

from base_user.models import MyUser
from django_countries.fields import CountryField
from base_app.models import CategoryModel, SubcategoryModel
# from CompanyApp.models import CompanyVacancy
from CompanyApp.models import SkillsModel
# Create your models here.
import datetime


class CountryModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CityModel(models.Model):
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CandidateCv(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    work_experience = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField()
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE,null=True, blank=True)
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE,null=True, blank=True)
    city_post = models.CharField(max_length=255, null=True,blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE,null=True,blank=True)
    headline = models.CharField(max_length=255, null=True,blank=True)
    # freelance = models.BooleanField(default=False)
    birthday = models.DateField(null=True,blank=True)
    phone = models.CharField(max_length=255, null=True,blank=True)
    document = models.FileField(upload_to='cv')

    def __str__(self):
        return self.user.username

class CandidateExpEdu(models.Model):
    cv = models.ForeignKey(CandidateCv, on_delete=models.CASCADE)
    EXPERIENCE = 'EXP'
    EDUCATION = 'EDU'

    exp_choices = [
        (EXPERIENCE, 'Experience'),
        (EDUCATION, 'Education'),
    ]
    exp_type = models.CharField(
        max_length=50,
        choices=exp_choices,
        default=None,
    )
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    present = models.BooleanField(default=False)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.cv.user.username

class CandidateSkills(models.Model):
    cv = models.ForeignKey(CandidateCv, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    skill_type = models.CharField(max_length=255)

# class CandidateSocialLinks(models.Model):
#     user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     url = models.CharField(max_length=300)
#
#     def __str__(self):
#         return self.user.username

class CandidatePortfolio(models.Model):
    cv = models.ForeignKey(CandidateCv, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.cv.user.username


class CandidatePost(models.Model):

    name = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255, null=True, blank=True)
    job_description = models.TextField()
    job_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    job_sub_category = models.ForeignKey(SubcategoryModel, on_delete=models.CASCADE)
    duration_flow = models.CharField(max_length=255)
    budget = models.IntegerField()
    approve_count = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    skills = models.ManyToManyField(SkillsModel, null=True, blank=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    create_date = models.DateField(default=datetime.datetime.now())
    def __str__(self):
        return self.name.username
    def get_image(self):
        if self.image:
            return self.image.url

    def save(self, *args, **kwargs):
        self.slug = slugify(self.job_title)
        super(CandidatePost, self).save(*args, **kwargs)


class CandidatePostImage(models.Model):
    post = models.ForeignKey(CandidatePost,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='workerimg')

    def __str__(self):
        return self.post.user.username



#
class LikeCandidate(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey('CompanyApp.CompanyVacancy', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
