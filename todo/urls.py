"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from todo.core import views
from todo.accounts import urls as accounts_urls

urlpatterns = [
    path(r"", views.home, name="core"),
    path(r"accounts/", include(accounts_urls, namespace="accounts")),
    path("admin/", admin.site.urls),
    # URL - TASKS
    path(r"add-task/", views.add_task, name="add_task"),
    re_path(r"delete-task/(?P<id_task>[0-9]+)/", views.delete_task, name="delete_task"),
    re_path(r"edit-task/(?P<id_task>[0-9]+)/", views.edit_task, name="edit_task"),
    # URLS - CATEGORIES
    path(r"categories/", views.list_categories, name="list_categories"),
    path(r"add-category/", views.add_category, name="add_category"),
    re_path(r"delete-category/(?P<id_category>[0-9]+)/", views.delete_category, name="delete_category"),
    re_path(r"edit-category/(?P<id_category>[0-9]+)/", views.edit_category, name="edit_category"),
]
