# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Region


class RegionAdmin(admin.ModelAdmin):
    fields = ("id", "code", "name", "parent", "grade")
    readonly_fields = ("id",)
    list_display = ("code", "name", "parent", "grade")
    list_filter = ("grade",)

admin.site.register(Region, RegionAdmin)

admin.site.site_header = "Region Date"
admin.site.site_title = "region"
admin.site.site_url ="/"
