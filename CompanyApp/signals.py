from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from .tasks import send_apply_email
from .models import ApplyCompany
from threading import Thread



@receiver(post_save, sender=ApplyCompany, dispatch_uid='send_mail_to_user')
def send_mail_to_user(*args, **kwargs):
    obj = kwargs.get("instance")
    created = kwargs.get("created")
    if created:
        link = f"http://localhost:8000/jobs/{obj.post.slug}/"
        link2 = f"http://localhost:8000/{obj.from_user.username}/about/"
        background_job = Thread(target=send_apply_email, args=(link2,obj.from_user.get_full_name(),obj.post.name.email, link,obj.post.job_title))
        background_job.start()