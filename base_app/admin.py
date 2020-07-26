from django.contrib import admin
from . import  models
# Register your models here.


admin.site.register(models.LeftMenu)
admin.site.register(models.RegisterModel)
admin.site.register(models.ButtonMenu)
admin.site.register(models.CategoryModel)
admin.site.register(models.SubcategoryModel)


class Candidateinline(admin.TabularInline):
    model = models.CandidateModel
    extra = 3


@admin.register(models.CompanyModel)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [Candidateinline]

@admin.register(models.CandidateModel)
class CandidateAdmin(admin.ModelAdmin):
    pass