# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    request.session['purchase'] = []
    return render(request, 'amadon/index.html')

def process(request):
    purchase = {}
    for key, value in request.POST.items():
        if key!="csrfmiddlewaretoken":
            purchase[key] = value

    if purchase['product_id'] == '10':
        purchase['product'] = 'Drone'
        purchase['total'] = int(purchase['quantity'])*59.99
    elif purchase['product_id'] == '20':
        purchase['product'] = 'Props'
        purchase['total'] = int(purchase['quantity'])*5.99
    elif purchase['product_id'] == '30':
        purchase['product'] = 'Motors'
        purchase['total'] = int(purchase['quantity'])*15.99
    else:
        purchase['product'] = 'ECM Board'
        purchase['total'] = int(purchase['quantity'])*19.99

    request.session['purchase'] = []
    request.session['purchase'] = purchase
    
    return redirect('/checkout')

def checkout(request):
    return render(request, 'amadon/checkout.html')
