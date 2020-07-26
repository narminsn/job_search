from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from . import forms
from . import models
import  requests
from base_app.views import common_data
from django.http import  HttpResponse, JsonResponse
from CompanyApp.forms import PostForm, CompanyProfileForms
from CompanyApp.models import CompanyVacancy, SkillsModel, AboutComp
from base_app.models import CategoryModel, SubcategoryModel
from base_user.models import MyUser
from CompanyApp.views import notifications
# Create your views here.



def settings_view(request):
    slug = request.user
    context = common_data()
    apply = notifications(request)
    context['notifications'] = apply
    if request.user.check == 'CAN':
        context['forms'] = forms.ProfileForms(instance=request.user)
        if request.method == 'POST':
            if 'image' in request.POST:
                img=request.FILES.get('img')
                a = request.user
                a.profile_image = img
                a.save()
                return redirect('profile_about' ,request.user)
            else:
                form = forms.ProfileForms(request.POST,request.FILES,instance=request.user)
                if form.is_valid():
                    cv = form.save(commit=False)
                    cv.user = request.user
                    cv.save()
                    return redirect('profile_about', request.user)
        if request.method == 'POST' and request.is_ajax():
            return JsonResponse({
                'asd' : 'df'
            })
            # country = request.POST.get('country')
            # countryModel = models.CountryModel.objects.filter(name=country)[0]
            # data = models.CityModel.objects.filter(country=countryModel)
            # result = []
            # for i in data:
            #     result.append(i.name)
            # return JsonResponse({
            #     'data' : result
            # })
    else:
        context['forms'] = CompanyProfileForms(instance=request.user)
        if request.method == 'POST':
            if 'image' in request.POST:
                img=request.FILES.get('img')
                a = request.user
                a.profile_image = img
                a.save()
                return redirect('candidate-profile', request.user)
            else:
                form = CompanyProfileForms(request.POST,request.FILES,instance=request.user)
                if form.is_valid():
                    cv = form.save(commit=False)
                    cv.user = request.user
                    cv.save()
                    return redirect('candidate-profile', request.user)
    return render(request, 'settings.html',context)

def cv_view(request):
    context = common_data()
    apply = notifications(request)
    context['notifications'] = apply
    CV = models.CandidateCv.objects.filter(user=request.user).last()
    context['CV'] = CV
    if CV:
        city = models.CityModel.objects.filter(country=models.CountryModel.objects.filter(name=CV.country)[0])
        context['cities'] = city
    # context['forms'] = forms.CvForms(initial={'work_experience': CV.work_experience, 'country': CV.country, 'about': CV.about, 'city_post':'dfg'})
    context['forms'] = forms.CvForms(instance=CV)
    if request.method == 'POST':
        if request.is_ajax():

            country = request.POST.get('country')
            countryModel = models.CountryModel.objects.filter(name=country)[0]
            data = models.CityModel.objects.filter(country=countryModel)
            result = []
            for i in data:
                obj={
                    'name' : i.name,
                    'id' : i.id
                }
                result.append(obj)
            return JsonResponse({
                'data' : result
            })
        else:
            form = forms.CvForms(request.POST, request.FILES, instance=CV)
            print('ASDFGHJK,M')
            print(request.POST.get('city'))
            if form.is_valid():

                cv = form.save(commit=False)
                cv.user_id = request.user.id
                cv.city = models.CityModel.objects.filter(id=request.POST.get('city')).last()
                cv.save()
                return redirect('profile_about', request.user)
            else:
                context['forms'] = form
    return render(request, 'cv.html', context)



def education_settings(request):
    slug = request.user
    context = common_data()
    apply = notifications(request)
    context['notifications'] = apply
    CV = request.user.candidatecv
    context['posts'] = models.CandidateExpEdu.objects.filter(cv=CV)
    context['forms'] = forms.EducationForms()
    if request.method == 'POST':
        if 'create' in request.POST:

            form = forms.EducationForms(request.POST)
            if form.is_valid():
                edu = form.save(commit=False)

                edu.cv = CV
                edu.save()
                return redirect("education-settings")
            else:
                context['forms']=form
        elif request.is_ajax():
            id = request.POST.get('id')
            return JsonResponse({
                'data': id
            })

    return render(request, 'education.html', context)


def skills_settings(request):
    context = common_data()
    apply = notifications(request)
    context['notifications'] = apply
    context['forms'] = forms.Skillforms()
    context['posts'] = request.user.candidatecv.candidateskills_set.all()
    if request.method == 'POST':
        form = forms.Skillforms(request.POST)
        if form.is_valid():
            CV = request.user.candidatecv
            skill = form.save(commit=False)
            skill.cv = CV
            skill.save()
            messages.success(
                request, "Ugurla elave edildi"
            )
            return redirect('settings-skil')

    return render(request, 'skillsettings.html', context)




def add_post_view(request):
    context = common_data()
    apply = notifications(request)
    context['notifications'] = apply
    if request.user.check == 'CAN':
        context['form'] = forms.PostForm
        skills = SkillsModel.objects.all()
        context['skills'] = skills
        if request.method == 'POST':
            skill = request.POST.getlist('skill')
            print(skill)
            print('ASDFGHJK')
            form = forms.PostForm(request.POST, request.FILES)
            image = request.FILES.get('imagee')
            if form.is_valid():
                print(skill)
                post = form.save(commit=False)
                post.name = request.user
                post.image = image
                post.save()
                for i in skill:
                    print('SKILLLL')
                    post.skills.add(i)

                return redirect('candidate-profile', request.user.slug)
            else:
                context['form'] = form
    else:
        context['form'] = PostForm
        skills = SkillsModel.objects.all()
        context['skills'] = skills
        if request.method == 'POST':
            skill = request.POST.getlist('skill')
            form = PostForm(request.POST, request.FILES)
            city = request.POST.get('city')
            image = request.FILES.get('imagee')


            if form.is_valid():
                post = form.save(commit=False)
                post.name = request.user
                city_model = models.CityModel.objects.filter(name=city).last()
                post.city = city_model
                post.image = 'https://www.elegantthemes.com/blog/wp-content/uploads/2019/06/featured-php-7.png'
                post.image_post = image
                print('IMAGEE')
                print(image)
                post.save()
                for i in skill:
                    post.skill.add(i)

                return redirect('candidate-profile', request.user.slug)

            else:
                context['form'] = form


    if request.method == 'POST' and request.is_ajax():
        country = request.POST.get('country')
        countryModel = models.CountryModel.objects.filter(id=int(country)).last()
        data = models.CityModel.objects.filter(country=countryModel)
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
        # country = request.POST.get('country')
        # countryModel = models.CountryModel.objects.filter(name=country)[0]
        # data = models.CityModel.objects.filter(country=countryModel)
        # result = []
        # for i in data:
        #     result.append(i.name)
        # return JsonResponse({
        #     'data' : result
        # })
    return render(request, 'add_postin.html', context)


def profile_view(request, user):
    context = common_data()
    apply = notifications(request)
    context['notifications'] = apply
    userid = MyUser.objects.filter(slug=user).last()
    if userid.check == 'CAN':

        pagination = Paginator(models.CandidatePost.objects.filter(name=userid).order_by('-id'), 12)


        context["jobs"] = pagination.get_page(request.GET.get('page', 1))
        context["page_range"] = pagination.page_range
    else:
        pagination = Paginator(CompanyVacancy.objects.filter(name=userid).order_by('-id'), 12)

        context["jobs"] = pagination.get_page(request.GET.get('page', 1))
        context["page_range"] = pagination.page_range
    context['userr'] = userid
    # if request.user.check == 'CAN':
    #     pagination = Paginator(models.CandidatePost.objects.filter(user=userid).order_by('-id'), 12)
    #     context["jobs"] = pagination.get_page(request.GET.get('page', 1))
    #     context["page_range"] = pagination.page_range
    #
    # else:
    #     context['about'] = AboutComp.objects.filter(user=request.user).last()
    #     pagination = Paginator(CompanyVacancy.objects.all().order_by('-id'), 12)
    #     context["jobs"] = pagination.get_page(request.GET.get('page', 1))
    #     context["page_range"] = pagination.page_range
    return render(request, 'candidate_profile.html', context)

def education_edit(request, id):
    context={}
    data = models.CandidateExpEdu.objects.filter(cv=request.user.candidatecv, id=id).last()
    if data:
        if request.method == 'POST':
            form = forms.EducationForms(request.POST, instance=data)
            if form.is_valid():
                form.save()
                messages.success(
                    request, "Ugurla update oldu"
                )
                return redirect('education-settings')
            else:
                messages.error(
                    request, f"Formda problem var {form.errors}"
                )
                return redirect('education-settings')
        context['edu'] = data
        context['forms'] = forms.EducationForms(instance=data)
        return render(request, 'include/education_form.html', context)

def education_delete(request, id):
    context = {}
    data = models.CandidateExpEdu.objects.filter(cv=request.user.candidatecv, id=id).last()
    if data:
        context['edu'] = data
        if request.method == 'DELETE':
            data.delete()
            return redirect('education-settings')
        else:
            pass
        return render(request, 'include/delete.html',context)




def skill_edit(request, id):
    context={}
    data = models.CandidateSkills.objects.filter(cv=request.user.candidatecv, id=id).last()

    if data:

        if request.method == 'POST':
            print('DATA')
            form = forms.Skillforms(request.POST, instance=data)
            if form.is_valid():
                form.save()
                print('SAVESAVEVSAVE')
                messages.success(
                    request, "Ugurla update oldu"
                )
                return redirect('settings-skil')
            else:
                messages.error(
                    request, f"Formda problem var {form.errors}"
                )
                return redirect('settings-skil')

        context['edu'] = data
        context['forms'] = forms.Skillforms(instance=data)
        return render(request, 'include/skills_form.html', context)

def skill_delete(request, id):
    context = {}
    data = models.CandidateSkills.objects.filter(cv=request.user.candidatecv, id=id).last()

    if data:

        context['edu'] = data
        if request.method == 'DELETE':
            data.delete()
            return redirect('settings-skil')
        else:
            pass
        return render(request, 'include/skill_delete.html',context)

def profile_about(request, user):
    context = common_data()
    apply = notifications(request)
    context['notifications'] = apply
    user = MyUser.objects.filter(slug=user).last()
    context['userr'] = user
    if user.check == 'CAN':

        user = MyUser.objects.filter(slug=user).last()
        CV = user.candidatecv
        skills = CV.candidateskills_set.all()
        exps = CV.candidateexpedu_set.all()
        context['user'] = user
        context['CV'] = CV
        context['exps'] = exps
        context['skills'] = skills
        context['job_count'] = user.candidatepost_set.all().count()

        return render(request, 'profile_about.html', context)
    else:
        context['user'] = user
        context['about'] = AboutComp.objects.filter(user=request.user).last()
        context['job_count'] = user.companyvacancy_set.all().count()
        context['about'] = user.aboutcomp_set.all().first()
        return render(request, 'company_listing_single.html',context)

