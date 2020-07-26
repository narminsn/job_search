from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='home' ),
    path('create/', views.create_view, name='create' ),
    path('about/',views.about_view, name='about')
]