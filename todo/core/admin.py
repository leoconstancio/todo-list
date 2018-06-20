from django.contrib import admin
from .models import Task, Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
admin.site.register(Category, CategoryAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "category", "date", "time", "description", "priority"]
admin.site.register(Task, TaskAdmin)
