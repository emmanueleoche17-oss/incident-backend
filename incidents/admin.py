from django.contrib import admin

from .models import Category, Incident


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "reporter", "status", "created_at")
    list_filter = ("status", "category", "created_at")
    search_fields = ("title", "description", "reporter__username")
    readonly_fields = ("created_at", "updated_at")
