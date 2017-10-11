from django.contrib import admin

from .models import Course, Module

class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ModuleInline]