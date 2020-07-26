from django.shortcuts import render, redirect
from base_app import models
from django.http import HttpResponse
from .models import VerificationModel
from . import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def common_data():
    context = {
        'buttons_menu': models.ButtonMenu.objects.all(),
        'leftmenu': models.LeftMenu.objects.all()
    }
    return context



# def register_view(request):
#     context = common_data()
#     context['company'] = forms.CompanyRegister
#     context['candidate'] = forms.CandidateRegister
#     if request.method == "POST":
#         if 'company' in request.POST:
#             form = forms.CompanyRegister(request.POST)
#             if form.is_valid():
#                 user = form.save(commit=False)
#                 # user.username = user.email
#                 user.set_password(request.POST.get('password1'))
#                 user.check = 'COM'
#                 user.is_active = False
#                 user.save()
#                 # messages.info(
#                 #     request, 'please verify your email'
#                 # )
#                 return HttpResponse("sdfgh")
#             else:
#                 context['company'] = form
#         else:
#             form = forms.CandidateRegister(request.POST)
#             if form.is_valid():
#                 user = form.save(commit=False)
#                 # user.username = user.email
#                 user.set_password(request.POST.get('password1'))
#                 user.check = 'CAN'
#                 user.is_active = False
#                 user.save()
#                 # messages.info(
#                 #     request, 'please verify your email'
#                 # )
#                 return HttpResponse("sdfgh")
#
#
#
#
#     return render(request, 'register.html',context)


def verify_view(request, token, user_id):
    verify = VerificationModel.objects.filter(token=token, user_id=user_id,expire_date=False).last()
    if verify:
        verify.expire_date = True
        verify.save()
        verify.user.is_active = True
        verify.user.save()
        messages.info(
            request, "Success"
        )
        return HttpResponse("active")
    else:
        return redirect('base-view')


#
# def login_view(request):
#     context = common_data()
#     context['loginform'] = forms.LoginForm
#     if not request.user.is_authenticated:
#
#         if request.method == "POST":
#             login_form = forms.LoginForm(request.POST)
#             if login_form.is_valid():
#
#                 username = login_form.cleaned_data.get('username')
#                 password = login_form.cleaned_data.get('password')
#                 user = authenticate(username=username, password=password)
#
#                 if user:
#                     if user.is_active:
#                         login(request, user)
#
#                         return HttpResponse('true')
#
#
#     return render(request, 'login.html', context)
#


def logout_view(request):
    logout(request)
    return redirect('home')