from django.db import models

# Create your models here.

class LeftMenu(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ButtonMenu(models.Model):
    name = models.CharField(max_length=255)
    icon_name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class RegisterModel(models.Model):
    image = models.ImageField(upload_to='home')
    background_image = models.ImageField(upload_to='home', null=True,blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class CategoryModel(models.Model):
    name = models.CharField(max_length=155)
    link = models.CharField(max_length=122)

    def __str__(self):
        return self.name

class SubcategoryModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class CompanyModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.name

class CandidateModel(models.Model):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE,related_name='candidate')
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=125)

    def __str__(self):
        return f'{self.company.name} => {self.first_name}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

