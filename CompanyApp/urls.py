from django.urls import path
from . import views
urlpatterns = [
    path('jobs/', views.jobs_view, name='jobs' ),
    # path('jobs/like', views.like_view, name='jobs'),
    # path('jobsd/', views.create, name='jobs'),
    path('jobs/<str:slug>/', views.CompanyPost, name='onepost'),
    path('like', views.post_like_view, name='likepost'),
    # path('search/', views.search_view, name='search_home'),
    # path('select/', views.search_list, name='search_list'),
    # path('<str:slug>/about/', views.comp_single, name = 'comp_single'),
    path('profile/settings/about/',views.comp_about_settings, name='comp_about_settings'),
    path('notif/delete/<int:id>', views.notif_delete, name='not_delete'),
    path('notif/accept/', views.notif_accept, name='not_accept'),
    # path('comp', views.companies, name='companies'),

]