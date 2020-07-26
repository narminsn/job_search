from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def send_apply_email(user_link,user,email, link,name):
    subject, from_email, to = 'Verificate Email', settings.EMAIL_HOST_USER, email
    text_content = 'Verificate Email'
    html_content = f'<p><a href="{user_link}">{user}</a> applied to your job post <a href="{link}">{name}</a> .</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()