from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.survey_list), 
    path('<slug:token>/', views.reply),
    path('<slug:token>/edit/', views.survey_edit),
    path('<slug:token>/summary/', views.reply_summary),
   
]