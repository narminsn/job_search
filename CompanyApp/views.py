import math

from django.shortcuts import render, redirect
from base_app.views import common_data
from django.contrib import messages
import requests
from . import models
from django.core.paginator import Paginator
from . import forms
from base_app.models import CategoryModel
from base_user.models import MyUser
from django.http import HttpResponse, JsonResponse
from base_app.models import CategoryModel, SubcategoryModel
from CandidateApp.models import CountryModel, CityModel
from django.db.models import Q
from CandidateApp.models import CandidatePost
import datetime
import  json

# Create your views here.

def notifications(request):
    if request.user.check == 'CAN':
        apply = request.user.companyy.all()
    else:
        apply = request.user.company.all()
    return apply



def comp_single(request,slug):
    return render(request,'company_listing_single.html')

# def jobs_view(request):
#     result = []
#
#     context = common_data()
#     if request.user.is_authenticated:
#         if request.user.check == 'CAN':
#             context['skills'] = models.SkillsModel.objects.all()
#             pagination = Paginator(models.CompanyVacancy.objects.all().order_by('-id'), 12)
#             context["jobs"] = pagination.get_page(request.GET.get('page', 1))
#             context["page_range"] = pagination.page_range
#             context['countries'] = CountryModel.objects.all()
#             context['category'] = CategoryModel.objects.all()
#             context['applies'] = [apply.post for apply in request.user.candidate.all()]
#             if 'search' in request.GET:
#                 title = request.GET['title']
#                 location = request.GET['location']
#                 category = request.GET['category']
#                 data = models.CompanyVacancy.objects.filter(
#                     # Q(job_title__icontains=title) |
#                     # Q(job_description__icontains=title) |
#                     Q(country_id=location) |
#                     Q(job_category_id=category)
#                 )
#                 # context['jobs'] = data
#                 print('ASDFGHJK')
#                 print(len(data))
#                 pagination = Paginator(data, 4)
#
#                 context["jobs"] = pagination.get_page(request.GET.get('page', 1))
#                 context["page_range"] = pagination.page_range
#
#                 try:
#                     page = int(request.GET.get('page', 0)) - 1
#                 except:
#                     page = 0
#
#                 context = {}
#                 limit = 3
#                 company_count = models.CompanyVacancy.objects.count()
#
#                 if page < 0:
#                     page = 0
#                 elif page > math.ceil(company_count / limit):
#                     page = math.ceil(company_count / limit) - 1
#
#                 context['selected_page'] = page + 1
#                 context['company_list'] = models.CompanyVacancy.objects.all()[page * limit:page * limit + limit]
#                 pages_count = math.ceil(company_count / limit)
#                 context['total_pages'] = range(1, pages_count + 1)
#                 context['horizontal_limit'] = 3
#                 context['next_page'] = page + 2 if page + 2 < pages_count else pages_count
#                 context['prev_page'] = page if page > 0 else 1
#
#             else:
#                 pass
#             if request.method == 'POST':
#
#                 if request.is_ajax():
#                     typee = request.POST.get("type")
#                     id = request.POST.get('text')
#                     name = json.loads(id)
#                     print(result)
#                     if typee == 'skills':
#                         for i in name:
#
#                             data = models.CompanyVacancy.objects.filter(skill=name[0])[:4]
#                             context['jobs'] = data
#                             result.append(data)
#                         print('LEN')
#                         print(len(data))
#                         print(len(result))
#                         return render(request, 'include/search_post.html', context)
#
#                     pagination = Paginator(result, 4)
#                     context["jobs"] = pagination.get_page(request.GET.get('page', 1))
#                     context["page_range"] = pagination.page_range
#                     context['applies'] = [apply.post for apply in request.user.applycompany_set.all()]
#
#                     return render(request, 'include/search_post.html', context)
#
#         else:
#             apply = notifications(request)
#             context['notifications'] = apply
#             context['skills'] = models.SkillsModel.objects.all()
#             pagination = Paginator(CandidatePost.objects.all().order_by('-id'), 12)
#             context["jobs"] = pagination.get_page(request.GET.get('page', 1))
#             context["page_range"] = pagination.page_range
#             context['countries'] = CountryModel.objects.all()
#             context['category'] = CategoryModel.objects.all()
#             if 'search' in request.GET:
#                 title = request.GET['title']
#                 category = request.GET['category']
#                 data = CandidatePost.objects.filter(
#                     # Q(job_title__icontains=title) |
#                     # Q(job_description__icontains=title) |
#
#                     Q(work_category_id=category)
#                 )
#                 # context['jobs'] = data
#                 print('ASDFGHJK')
#                 print(len(data))
#                 pagination = Paginator(data, 4)
#                 context["jobs"] = pagination.get_page(request.GET.get('page', 1))
#                 context["page_range"] = pagination.page_range
#
#
#
#             else:
#
#                 pass
#             # context['applies'] = [apply.post for apply in request.user.applycompany_set.all()]
#     else:
#
#         pagination = Paginator(models.CompanyVacancy.objects.all().order_by('-id'), 12)
#
#         context["jobs"] = pagination.get_page(request.GET.get('page', 1))
#         context["page_range"] = pagination.page_range
#
#     return render(request, 'listing_left.html', context)

# CompanyVacancy.objects.all().prefetch_related('skillsmodels')
# len([list(skil.skill.filter(name='Python')) for skil in comps])

# JOBS
def jobs_view(request):
    result = []

    context = common_data()
    context['active'] = 'jobs'
    if request.user.is_authenticated:
        if request.user.check == 'CAN':
            apply = notifications(request)
            context['notifications'] = apply
            context['skills'] = models.SkillsModel.objects.all()
            pagination = Paginator(models.CompanyVacancy.objects.all().order_by('-id'), 12)
            context["jobs"] = pagination.get_page(request.GET.get('page', 1))
            context["page_range"] = pagination.page_range
            context['countries'] = CountryModel.objects.all()
            context['category'] = CategoryModel.objects.all()
            context['applies'] = [apply.post for apply in request.user.candidate.all()]
            context['appliescan'] = [apply.post_can for apply in request.user.candidatee.all()]

            if 'search' in request.GET:
                title = request.GET['title']
                location = request.GET['location']
                category = request.GET['category']
                data = models.CompanyVacancy.objects.filter(
                    # Q(job_title__icontains=title) |
                    # Q(job_description__icontains=title) |
                    Q(country_id=location) |
                    Q(job_category_id=category)
                )[:8]
                # context['jobs'] = data
                print('ASDFGHJK')
                print(len(data))
                pagination = Paginator(data, 8)

                context["jobs"] = pagination.get_page(request.GET.get('page', 1))
                context["page_range"] = pagination.page_range


            if request.method == 'POST':

                if request.is_ajax():
                    print("AJAX")

                    typee = request.POST.get("type")
                    id = request.POST.get('text')
                    print(id)

                    if typee == 'skills':
                        data = models.CompanyVacancy.objects.filter(skill = int(id) )[:4]
                        for i in data:
                            obj = {
                                'type' : id,
                                'image' : i.image,
                                'job_title' : i.job_title,
                                'country' : i.country.name,
                                'city' : i.city.name,
                                'max_salary' : i.max_salary,
                                'min_salary' : i.min_salary,
                                'id' : i.id
                            }
                            result.append(obj)
                        return JsonResponse({
                            'data' : result
                        })
                    elif typee == 'parttime':
                        if id == 'c33':
                            data = models.CompanyVacancy.objects.all()[:4]
                            for i in data:
                                obj = {
                                    'type': id,
                                    'image': i.image,
                                    'job_title': i.job_title,
                                    'country': i.country.name,
                                    'city': i.city.name,
                                    'max_salary': i.max_salary,
                                    'min_salary': i.min_salary,
                                    'id': i.id
                                }
                                result.append(obj)
                            return JsonResponse({
                                'data': result
                            })
                        elif id == 'c34':
                            data = models.CompanyVacancy.objects.all()[6:10]
                            for i in data:
                                obj = {
                                    'type': id,
                                    'image': i.image,
                                    'job_title': i.job_title,
                                    'country': i.country.name,
                                    'city': i.city.name,
                                    'max_salary': i.max_salary,
                                    'min_salary': i.min_salary,
                                    'id': i.id
                                }
                                result.append(obj)
                            return JsonResponse({
                                'data': result
                            })
                        elif id == 'c35':
                            data = models.CompanyVacancy.objects.all()[14:18]
                            for i in data:
                                obj = {
                                    'type': id,
                                    'image': i.image,
                                    'job_title': i.job_title,
                                    'country': i.country.name,
                                    'city': i.city.name,
                                    'max_salary': i.max_salary,
                                    'min_salary': i.min_salary,
                                    'id': i.id
                                }
                                result.append(obj)
                            return JsonResponse({
                                'data': result
                            })
                        elif id == 'c36':
                            data = models.CompanyVacancy.objects.all()[20:24]
                            for i in data:
                                obj = {
                                    'type': id,
                                    'image': i.image,
                                    'job_title': i.job_title,
                                    'country': i.country.name,
                                    'city': i.city.name,
                                    'max_salary': i.max_salary,
                                    'min_salary': i.min_salary,
                                    'id': i.id
                                }
                                result.append(obj)
                            return JsonResponse({
                                'data': result
                            })

                        elif id == 'c37':
                            data = models.CompanyVacancy.objects.all()[34:38]
                            for i in data:
                                obj = {
                                    'type': id,
                                    'image': i.image,
                                    'job_title': i.job_title,
                                    'country': i.country.name,
                                    'city': i.city.name,
                                    'max_salary': i.max_salary,
                                    'min_salary': i.min_salary,
                                    'id': i.id
                                }
                                result.append(obj)
                            return JsonResponse({
                                'data': result
                            })




        else:
            context['appliescan'] = [apply.post_can for apply in request.user.candidatee.all()]

            apply = notifications(request)
            context['notifications'] = apply
            context['skills'] = models.SkillsModel.objects.all()
            pagination = Paginator(CandidatePost.objects.all().order_by('-id'), 12)
            context["jobs"] = pagination.get_page(request.GET.get('page', 1))
            context["page_range"] = pagination.page_range
            context['countries'] = CountryModel.objects.all()
            context['category'] = CategoryModel.objects.all()
            if 'search' in request.GET:
                title = request.GET['title']
                category = request.GET['category']
                data = CandidatePost.objects.filter(
                    # Q(job_title__icontains=title) |
                    # Q(job_description__icontains=title) |

                    Q(job_category_id=category)
                )
                # context['jobs'] = data
                print('ASDFGHJK')
                print(len(data))
                pagination = Paginator(data, 4)

                context["jobs"] = pagination.get_page(request.GET.get('page', 1))
                context["page_range"] = pagination.page_range

            if request.method == 'POST':

                if request.is_ajax():
                    print("AJAX")

                    typee = request.POST.get("type")
                    id = request.POST.get('text')
                    print(id)

                    if typee == 'skills':
                        data = CandidatePost.objects.all()[:2]
                        for i in data:
                            obj = {
                                'type' : id,
                                'image' : i.image.url,
                                'job_title' : i.job_title,
                                'category' : i.job_category.name,
                                'subcategory' : i.job_sub_category.name,
                                'budget' : i.budget,
                                # 'min_salary' : i.min_salary,
                                'id' : i.id
                            }
                            result.append(obj)
                        return JsonResponse({
                            'data' : result
                        })



                    #     for i in name:
                    #
                    #         data = models.CompanyVacancy.objects.filter(skill=name[0])[:4]
                    #         context['jobs'] = data
                    #         result.append(data)
                    #     print('LEN')
                    #     print(len(data))
                    #     print(len(result))
                    #     return render(request, 'include/search_post.html', context)
                    #
                    # pagination = Paginator(result, 4)
                    # context["jobs"] = pagination.get_page(request.GET.get('page', 1))
                    # context["page_range"] = pagination.page_range
                    # context['applies'] = [apply.post for apply in request.user.applycompany_set.all()]
                    #
                    # return render(request, 'include/search_post.html', context)
            # context['applies'] = [apply.post for apply in request.user.applycompany_set.all()]
    else:
        pagination = Paginator(models.CompanyVacancy.objects.all().order_by('-id'), 12)

        context["jobs"] = pagination.get_page(request.GET.get('page', 1))
        context["page_range"] = pagination.page_range

    return render(request, 'listing_left.html', context)



# def like_view(request):
#     if request.method == 'POST' and request.is_ajax():
#         if request.user.check == 'CAN':
#             posts = models.CompanyVacancy.objects.all()
#         else:
#             posts = CandidatePost.objects.all()
#         post_id = request.POST.get('id')
#
#         post = posts.filter(id=post_id)[0]
#         if post:
#             print('LIKE')
#             print(request.user.id)
#             print(post_id)
#             print(post.id)
#             if request.user.check == 'CAN':
#                 like = LikeModel.objects.filter(user_id=request.user.id,post_id=post.id)
#             else:
#                 like = models.LikeCompany.objects.filter(user_id=request.user.id,post_id=post.id).last()
#             if like:
#                 like.delete()
#             else:
#                 print(post_id)
#                 if request.user.check == 'CAN':
#                     LikeModel.objects.create(
#                         user=request.user,
#                         post=post
#                     )
#                 else:
#                     models.LikeCompany.objects.create(
#                         user=request.user,
#                         post=post
#                     )
#         return JsonResponse({
#             'status' : 'oke'
#         })


# def create_view(request):
#     country = ['United States', 'New Zealand', 'Hungary', 'Austria', 'Denmark',
#                'Montenegro', 'Japan', 'Finland', 'Croatia', 'United States']
#     cities = ['Florida', 'Wellington', 'Budapest', 'Salzburg', 'Zealand',
#               'Bijelo Polje', 'Tokushima', 'Pirkanmaa', 'Požeško-Slavonska', 'Pennsylvania']
#     data = list(models.CompanyVacancy.objects.all())[88:98]
#     # data.country = CountryModel.objects.filter(name=country[0])[0]
#     # data.save()
#     for index, value in enumerate(data):
#         print(index)
#         print(value.country)
#         value.country=CountryModel.objects.filter(name=country[index])[0]
#         value.save()
#         value.city=CityModel.objects.filter(name=cities[index])[0]
#         value.save()
#     # for index, value in enumerate(data):
#     #     print(index)
#     #     print(value)
#     #     value.country =CountryModel.objects.filter(name=country[0])[0],
#     #     # value.city=CityModel.objects.filter(name=cities[0])[0]
#     #     value.save()
#
#     return HttpResponse('success')

#     skill = [
#         {
#             "languages": ["english", "french", "arabic",
#                           "Portuguese", "turkish", "Kannada", "Vietnamese"
#                           ],
#             "Programming Language": [
#                 "Javascript", "Php", "Java", "Html5", "Css"
#                 , "Python", "C++"
#             ]
#         }
#     ]
#     response = requests.get('https://jobs.github.com/positions.json?description=ruby&page=1')
#     data = response.json()
#     for index, value in enumerate(data[10:20]):
#         models.CompanyVacancy.objects.create(name=request.user, job_types='Full Time', job_title=value['title'],
#                                              job_category=
#                                              CategoryModel.objects.filter(name='Programming & Tech')[0],
#                                              job_sub_category=SubcategoryModel.objects.filter(name='QA')[
#                                                  0],
#                                              country=CountryModel.objects.filter(name=country[index])[0],
#                                              city=CityModel.objects.filter(name=cities[index])[0],
#                                              max_salary='2500 EUR', min_salary='1000 EUR',
#                                              skills='Python, Javascript, Php, Html5, Css, Sql, Redis, C++, Java, Ruby,  English, French, Russian',
#                                              job_description=value['description']
#                                              )
#     return HttpResponse("create")


# def create(request):
#     data =CandidatePost.objects.all()
#     # skill = ['27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39']
#
#     for i in data:
#         i.save()
#         # i.skill.add(skill[3],skill[2],skill[9],skill[12],skill[11])
#
#     return HttpResponse("success")


def CompanyPost(request, slug):  # slug a kecirersen
    context = common_data()
    apply = notifications(request)
    context['notifications'] = apply
    context['applies'] = [apply.post for apply in request.user.candidate.all()]
    post = models.CompanyVacancy.objects.filter(slug=slug).last()
    if post:
        context['post'] = post
    else:
        context['post'] = CandidatePost.objects.filter(slug=slug).last()
    # date_post = post.create_date.strftime('%m,%d,%Y')
    # context['date'] = date_post
    # context['country'] = post.country.name
    # context['city'] = post.city.name


    return render(request, 'listing_single.html', context)


def post_like_view(request):
    if request.method == 'POST':

        id = request.POST.get('text')
        if request.user.check == 'CAN':
            post = models.CompanyVacancy.objects.filter(id=id).last()

            apply = models.ApplyCompany.objects.filter(from_user=request.user, post=post, to_user=post.name)
            if apply:

                apply.delete()
                return JsonResponse({
                    'status': False
                })
            else:

                models.ApplyCompany.objects.create(
                    from_user=request.user,
                    to_user=post.name,
                    post=post
                )
                return JsonResponse({
                    'status': True
                })

        else:

            post = CandidatePost.objects.filter(id=id).last()

            apply =models.ApplyCandidate.objects.filter(from_user=request.user, post_can=post, to_user=post.name)

            if apply:

                apply.delete()
                return JsonResponse({
                    'status': False
                })
            else:

                models.ApplyCandidate.objects.create(
                    from_user=request.user,
                    to_user=post.name,
                    post_can=post
                )
                return JsonResponse({
                    'status': True
                })


# def search_view(request):
#     context = common_data()
#     category = CategoryModel.objects.all()
#     context['categories'] = category
#
#     context['countries'] = CountryModel.objects.all()
#     context['category'] = CategoryModel.objects.all()
#     if 'search' in request.GET:
#         title = request.GET['title']
#         location = request.GET['location']
#         category = request.GET['category']
#         data = models.CompanyVacancy.objects.filter(
#             Q(job_title__icontains=title) |
#             Q(job_description__icontains=title) |
#             Q(country_id=location) |
#             Q(job_category_id=category)
#         )
#         context['jobs'] = data
#         messages.success(request, f"{len(data)} results found for you")
#
#     return render(request, 'log_home.html', context)
#
# #
def search_list(request):
    return render(request, 'time.html')



def comp_about_settings(request):
    context = common_data()
    apply = notifications(request)
    context['notifications'] = apply
    if request.user.check == "COM":
        data = models.AboutComp.objects.filter(user=request.user).last()
        context['forms'] = forms.Comp_About(instance=data)
        if request.method == 'POST':
            form = forms.Comp_About(request.POST, instance=data)
            if form.is_valid():
                about = form.save(commit=False)
                about.user = request.user
                about.save()
                return redirect('candidate-profile', request.user)
            else:
                context['forms'] = form
    # else:

    return render(request, 'comp_about_settings.html',context)

def notif_delete(request,id):
    if request.user.check == 'CAN':

        apply = models.ApplyCandidate.objects.filter(id=id).last()
        apply.delete()

    else:

        apply = models.ApplyCompany.objects.filter(id=id).last()
        apply.delete()


    return JsonResponse({
        'status' : True
    })

def notif_accept(request):
    id = request.POST.get('id')
    if request.user.check == 'CAN':
        apply = models.ApplyCandidate.objects.filter(id=id).last()
        apply.accepted = True
        apply.save()
    else:

        apply = models.ApplyCompany.objects.filter(id=id).last()
        apply.accepted=True
        apply.save()



    return JsonResponse({
        'status' : True
    })



def companies(request):
    try:
        start = int(request.GET.get('start', 0)) - 1
    except:
        start = 0
    print(start)
    context = {}
    limit = 3
    company_count = models.CompanyVacancy.objects.count()

    if start < 0:
        start = 0
    elif start > math.ceil(company_count / limit):
        start = math.ceil(company_count / limit) - 1

    context['selected_page'] = start + 1
    context['company_list'] = models.CompanyVacancy.objects.all()[start * limit:start * limit + limit]
    pages_count = math.ceil(company_count / limit)
    context['total_pages'] = range(1, pages_count + 1)
    context['horizontal_limit'] = 3
    context['next_page'] = start + 2 if start + 2 < pages_count else pages_count
    context['prev_page'] = start if start > 0 else 1

    return render(request, "companies.html", context)
