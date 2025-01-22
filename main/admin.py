from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from ckeditor.widgets import CKEditorWidget
from django.db import models
from .models import Seller, Category, Tag, Ad


class FlatPageCustomAdmin(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }


class SellerAdmin(admin.ModelAdmin):
    list_display = ("published_ads_count",)


admin.site.unregister(FlatPage)  # Убираем стандартную регистрацию
# Регистрируем с новым классом
admin.site.register(FlatPage, FlatPageCustomAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Ad)
