from django.urls import path
from . import views
urlpatterns = [
    path('profile/settings/', views.settings_view, name='settings_candidate' ),
    path('profile/education/', views.education_settings, name='education-settings'),
    path('profile/skills/', views.skills_settings, name='settings-skil'),
    # path('city/', views.create/),
    path('addingpost/', views.add_post_view, name='add_post'),
    path('<str:user>/posts/', views.profile_view, name='candidate-profile'),
    path('profile/education/<int:id>/edit/', views.education_edit, name='edu_edit'),
    path('profile/education/<int:id>/delete/', views.education_delete, name='edu_delete'),
    path('profile/cv/', views.cv_view, name='can_cv'),
    path('profile/skill/<int:id>/edit/', views.skill_edit, name='skill_edit'),
    path('profile/skill/<int:id>/delete/', views.skill_delete, name='skill_delete'),
    path('<str:user>/about/',views.profile_about, name='profile_about')

]