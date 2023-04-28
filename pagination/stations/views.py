from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    bus_st = []
    with open(settings.BUS_STATION_CSV, 'r', encoding='utf-8') as csvfile:
        station = csv.reader(csvfile)
        for idx, r in enumerate(station):
            if idx != 0:
                bus_st.append({'Name': r[1], 'Street': r[4], 'District': r[6]})
    paginator = Paginator(bus_st, 10)
    page = paginator.get_page(int(request.GET.get('page', 1)))
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
