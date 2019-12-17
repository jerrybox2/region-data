# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import JsonResponse
from django.shortcuts import render

from .models import Region, populate_tree


def get_provinces(request):
    province = Region.objects.filter(parent=None)


def get_citys(request, code):
    children = Region.objects.filter(code=code).children.all()


def get_region(request, grade="province", deepth=1):
    provinces = Region.objects.filter(parent=None).get(code="130000")
    data = populate_tree(provinces, grade="county")
    context = {"data": data}
    return JsonResponse(context)
