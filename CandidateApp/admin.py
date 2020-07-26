from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.CandidateCv)
admin.site.register(models.CandidateExpEdu)
admin.site.register(models.CandidateSkills)
admin.site.register(models.CandidatePortfolio)
admin.site.register(models.CandidatePost)
admin.site.register(models.CandidatePostImage)
admin.site.register(models.CountryModel)
admin.site.register(models.CityModel)
admin.site.register(models.LikeCandidate)

# admin.site.register(models.Person)