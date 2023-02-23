from django.contrib import admin
from .models import AppModel


class AppModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'status')


admin.site.register(AppModel, AppModelAdmin)
# Register your models here.
