from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from . import models
from base_user.models import MyUser


class ProfileForms(forms.ModelForm):
    # profile_image = forms.ImageField()
    class Meta:
        model = MyUser
        fields = [
            'first_name', 'last_name' , 'username'
         ]

class EducationForms(forms.ModelForm):

    class Meta:
        model = models.CandidateExpEdu
        fields = [
            'exp_type', 'name', 'start_date', 'end_date' , 'description'
        ]

        widgets = {
            'start_date': forms.TextInput(attrs={
                'class': 'timepicker'
            })
        }

class Skillforms(forms.ModelForm):
    class Meta:
        model = models.CandidateSkills
        fields = [
            'name', 'skill_type'
        ]

class PostForm(forms.ModelForm):
    class Meta:
        model = models.CandidatePost
        fields = ['job_title', 'job_category', 'job_sub_category', 'skills', 'duration_flow', 'budget', 'image', 'job_description']



class CvForms(forms.ModelForm):
    class Meta:
        model = models.CandidateCv
        fields = ['work_experience', 'country', 'city_post', 'category', 'headline', 'birthday', 'phone',  'about']