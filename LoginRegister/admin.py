# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from import_export.admin import ImportExportModelAdmin
from .models import CompanyDetails
from django.contrib import admin

# Register your models here.
@admin.register(CompanyDetails)
class CompanyDetailsAdmin(ImportExportModelAdmin):
    pass
    