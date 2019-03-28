# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Category, Article


class ArticleAdmin(admin.ModelAdmin):
    fields = ("id", "name", "content", "category")
    readonly_fields = ("id",)
    list_display = ("name", "content", "category")


class CategoryAdmin(admin.ModelAdmin):
    fields = ("id", "name",)
    readonly_fields = ("id",)
    list_display = ("name",)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_header = "Djang Project Sample"
admin.site.site_title = "sample"
admin.site.site_url ="/"
