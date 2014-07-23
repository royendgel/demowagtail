from django.contrib import admin
from .models import HomePageTranslation
from demo.models import HomePage


class HomePageTranslationInline(admin.StackedInline):
    model = HomePageTranslation


class HomePageAdmin(admin.ModelAdmin):
    inlines = [HomePageTranslationInline]


admin.site.register(HomePage, HomePageAdmin)
