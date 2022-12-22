from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('countries_list/', views.countries_list),
    path('languages_list/', views.languages),
    path('languages_list/<str:language>', views.languages_countries),
    path('countries_list/<str:country_name>', views.country),
    path('countries_list/speaking_countries/<str:language>', views.language_in_countries)
]
