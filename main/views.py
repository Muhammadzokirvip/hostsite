from django.shortcuts import render
from . import models


def index(request):
    baner = models.Banner.objects.last()
    about_us = models.AboutUs.objects.last()
    services = models.Service.objects.all()

    prices_list = []

    for price in models.Price.objects.all().order_by('price'):
        price.body = price.body.split(',')
        prices_list.append(price)

    context = {
        'baner':baner,
        'about_us':about_us,
        'services':services,
        'prices':prices_list
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == 'POST':
        try:
            models.Contact.objects.create(
                name=request.POST['name'],
                phone=request.POST['phone'],
                email=request.POST['email'],
                body=request.POST['message']
            )
        except:
            ...
    return render(request, 'contact.html')

def service(request):
    return render (request, 'service.html')

def about(request):
    return render (request, 'about.html')

def price(request):
    prices_list = []

    for price in models.Price.objects.all().order_by('price'):
        price.body = price.body.split(',')
        prices_list.append(price)
    return render (request, 'price.html')