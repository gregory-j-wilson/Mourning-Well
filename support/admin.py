from django.contrib import admin
from .models import Prompt, Resource, JournalEntry


@admin.register(Prompt)
class PromptAdmin(admin.ModelAdmin):
    list_display = ("text", "stage", "created")
    list_filter = ("stage",)
    search_fields = ("text",)


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ("title", "kind", "phone")
    list_filter = ("kind",)
    search_fields = ("title", "description")


@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ("__str__", "prompt", "created")
    readonly_fields = ("session_key", "created")
