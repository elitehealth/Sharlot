from django.shortcuts import render_to_response
from django.views.generic import ListView
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import redirect,  get_object_or_404
from django.contrib import auth
from django.contrib.auth import models
from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.db import connection
import sqlite3, random, os, json
from django.shortcuts import render
from django.db.models import Avg, Max, Min,F, FloatField, Sum,Count
import datetime
from .forms import AddInventoryForm, ProductTypeForm, InventoryForm, SupplierForm

def home(request):
    return render(request, 'base.html',{})

def profile(request):
    return render(request, 'templates/index.html',{})


def add_producttype(request):

    if request.user.is_authenticated():
        form = ProductTypeForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()

        context = {
        "form": form
        }
        return render(request, 'templates/form_product.html', context)

    else:
        return render(request, 'base.html',{})

def add_productmodel(request):

    if request.user.is_authenticated():
        form = InventoryForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()

        context = {
        "form": form
        }
        return render(request, 'templates/form_product_model.html', context)

    else:
        return render(request, 'base.html',{})



def add_supplier(request):

    if request.user.is_authenticated():
        form = SupplierForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()

        context = {
        "form": form
        }
        return render(request, 'templates/form_supplier.html', context)

    else:
        return render(request, 'base.html',{})

def add_inventory(request):

    if request.user.is_authenticated():
        form = AddInventoryForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()

        context = {
        "form": form
        }
        return render(request, 'templates/form_add_inventory.html', context)

    else:
        return render(request, 'base.html',{})

