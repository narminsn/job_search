from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from base_user.models import MyUser
from CandidateApp.models import CityModel, CountryModel
from . import models
from base_user.forms import CandidateRegister, CompanyRegister, LoginForm
from django.contrib.auth import authenticate, login, logout
from CompanyApp.models import CompanyVacancy

# Create your views here.

def common_data():
    context = {
        'buttons_menu': models.ButtonMenu.objects.all(),
        'leftmenu': models.LeftMenu.objects.all(),

    }
    return context

def notifications(request):
    if request.user.check == 'CAN':
        apply = request.user.companyy.all()
    else:
        apply = request.user.company.all()
    return apply


def home_view(request):
    context = common_data()
    context['active'] = 'home'
    context['company'] = CompanyRegister
    context['candidate'] = CandidateRegister
    context['loginform'] = LoginForm
    context['categories'] = models.CategoryModel.objects.all()
    context['posts'] = CompanyVacancy.objects.all()[:4]
    if not request.user.is_authenticated:

        if request.method == "POST":
            if request.is_ajax():

                country = request.POST.get('country')
                countryModel = CountryModel.objects.filter(id=int(country)).last()
                data = CityModel.objects.filter(country=countryModel)
                result = []
                for i in data:
                    obj = {
                        'name': i.name,
                        'id': i.id
                    }
                    result.append(obj)
                return JsonResponse({
                    'data': result
                })
            if 'company' in request.POST:
                form = CompanyRegister(request.POST)
                if form.is_valid():
                    user = form.save(commit=False)
                    # user.username = user.email
                    user.set_password(request.POST.get('password1'))
                    user.check = 'COM'
                    user.city = CityModel.objects.filter(id=request.POST.get('city')).last()
                    user.is_active = False
                    user.save()
                    messages.info(
                        request, 'please verify your email'
                    )
                    return redirect('home')
                else:
                    context['company'] = form
            elif 'candidate' in request.POST:
                print('ASDGRHJM')
                form = CandidateRegister(request.POST)
                if form.is_valid():
                    user = form.save(commit=False)
                    # user.username = user.email
                    user.set_password(request.POST.get('password1'))
                    user.check = 'CAN'
                    user.is_active = False
                    user.save()
                    messages.info(
                        request, 'please verify your email'
                    )
                    return redirect('home')
                else:
                    context['candidate'] = form
            else:
                login_form = LoginForm(request.POST)
                if login_form.is_valid():

                    username = login_form.cleaned_data.get('username')
                    password = login_form.cleaned_data.get('password')
                    user = authenticate(username=username, password=password)

                    if user:
                        if user.is_active:
                            login(request, user)

                            return redirect('home')
    else:
        apply = notifications(request)
        context['notifications'] = apply
    context['comps'] = MyUser.objects.filter(check='COM')[1:]

    return render(request, 'home.html', context)
    #
    # else:
    #     return redirect('jobs')


def create_view(request):
    a = ['Graphics & Design', 'Video & Animation',
         'Programming & Tech', 'Digital Marketing', 'Writing & Translation']
    b = ['WordPress', 'Website Builders & CMS', 'Game Development', 'Web Programming',
         'E-Commerce Development',
         'Mobile Apps', 'Desktop Application', 'Support It',
         'Data Analysis & Reports', 'Convert Files', 'Databases',
         'User Testing', 'QA']
    category = models.CategoryModel.objects.get(name='Programming & Tech')
    for i in b:
        models.SubcategoryModel.objects.create(category=category, name=i, link=f'{i}/')
    return HttpResponse('success')


def about_view(request):
    context = common_data()
    context['active'] = 'about'
    if request.user.is_authenticated:
        apply = notifications(request)
        context['notifications'] = apply
    return render(request, 'about.html', context)
