from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from ckeditor.widgets import CKEditorWidget
from django.db import models

class FlatPageCustomAdmin(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

admin.site.unregister(FlatPage)  # Убираем стандартную регистрацию
admin.site.register(FlatPage, FlatPageCustomAdmin)  # Регистрируем с новым классом
