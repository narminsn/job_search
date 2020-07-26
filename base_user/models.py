from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin, UserManager
import random
import  string
#
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.conf import settings
# User = get_user_model()
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
#
#
USER_MODEL =settings.AUTH_USER_MODEL
#
#
class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100,unique=True)
    first_name = models.CharField(_('Name'), max_length=255,null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile', null=True, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=255,null=True, blank=True)
    company_name = models.CharField(_('Company Name'), null=True, max_length=255, blank=True)
    country = models.ForeignKey("CandidateApp.CountryModel", on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey("CandidateApp.CityModel", on_delete=models.CASCADE, null=True, blank=True)
    city_post = models.CharField(max_length=255, null=True, blank=True)
    headline = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    # check = models.BooleanField(default=False)
    USER_CHOICES = (
        ('COM', 'COMPANY'),
        ('CAN', 'CANDIDATE'),
    )
    check = models.CharField(max_length=3, choices=USER_CHOICES)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    is_superuser = models.BooleanField(_("superuser"), default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    # is_anonymous = False
    is_authenticated = True

    objects = UserManager()
    # EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return "{}".format(self.username)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def get_image(self):
        if self.profile_image:
            return self.profile_image.url

        else:
            return 'https://forwardsummit.ca/wp-content/uploads/2019/01/avatar-default.png'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        # unique_together = ("username", "email")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(MyUser, self).save(*args, **kwargs)


def generate_token(size=120, chars=string.ascii_letters + string.digits):
    return  "".join(random.choice(chars) for i in range(size))


class VerificationModel(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=120, default=generate_token)
    expire_date = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.token}"