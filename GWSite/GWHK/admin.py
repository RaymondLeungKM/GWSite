from django.contrib import admin
from .models import jobOpenings, pressRelease, companyNews

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class JobOpeningsAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(jobOpenings, JobOpeningsAdmin)

class PressReleaseAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(pressRelease, PressReleaseAdmin)

class CompanyNewsAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(companyNews, CompanyNewsAdmin)