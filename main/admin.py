from django.contrib import admin
from .models import Tutorial
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
    # fields = ["tutorial_title", "tutorial_content", "tutorial_published"]
    fieldsets = [
    ("Title/Date", {"fields": (["tutorial_title", "tutorial_published"])}),
    ("content",{"fields":(["tutorial_content"])})
    ]
    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Tutorial, TutorialAdmin)