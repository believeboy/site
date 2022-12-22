import json
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
import string

with open('data/country-by-languages.json') as f:
    countries_db = json.load(f)

letters = string.ascii_uppercase


def home(request):
    return render(request, 'first_page.html')


def countries_list(request):
    countries = []
    for countries_b in countries_db:
        countries.append(countries_b['country'])
    word = request.GET.get('word')
    if word:
        countries = list(filter(lambda name: name[0] == word, countries))
    countries = sorted(countries)
    pagination = Paginator(countries, 10)
    page_number = request.GET.get('page')
    page_countries = pagination.get_page(page_number)
    return render(request, 'countries_list.html', {'page_countries': page_countries, 'letters': letters, 'word': word})


def languages(request):
    languages_list = set()
    for l in countries_db:
        languages_list.update(l['languages'])

    return render(request, 'languages_page.html', {'languages': sorted(languages_list)})


def country(request, country_name):
    info_about_country = {}

    for country_inf in countries_db:
        if country_inf['country'] == country_name:
            info_about_country['country'] = country_inf['country']
            info_about_country['languages'] = country_inf['languages']
            return render(request, 'country_page.html', {'country': info_about_country})


def language_in_countries(request, language):
    country_name = []
    for countries in countries_db:
        if language in countries['languages']:
            country_name.append(countries['country'])
    country_names = country_name
    return render(request, 'language_in_countries.html', {'country': country_names, 'language': language})


def languages_countries(request, language):
    country_name = []
    for countries in countries_db:
        if language in countries['languages']:
            country_name.append(countries['country'])
    country_names = country_name
    return render(request, 'language_in_countries.html', {'country': country_names, 'language': language})
