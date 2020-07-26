from django import forms
from . import  models
from base_user.models import MyUser
class PostForm(forms.ModelForm):
    class Meta:
        model = models.CompanyVacancy
        fields = ['job_title', 'job_category', 'job_sub_category', 'job_types', 'country',
                   'city_post', 'skill', 'min_salary', 'max_salary',
                  'image_post',  'job_description']


class CompanyProfileForms(forms.ModelForm):
    # profile_image = forms.ImageField()
    class Meta:
        model = MyUser
        fields = [
            'company_name',  'username', 'email'
         ]


class Comp_About(forms.ModelForm):
    class Meta:
        model = models.AboutComp
        fields = [
            'category','headline','experience', 'about'
        ]