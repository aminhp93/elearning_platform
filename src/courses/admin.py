from django.contrib import admin

from .models import Category, Course, Module

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	prepopulated_field = {'slug': ('title', )}


class ModuleInline(admin.StackedInline):
	model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ['title', 'created']
	inlines = [ModuleInline]