from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import TaskForm, CategoryForm
from .models import Task, Category
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def home(request):
    count_tasks = Task.objects.filter(user=request.user).count()
    list_tasks = Task.objects.filter(user=request.user)
    return render(request, "core/index.html", {
        "count_tasks": count_tasks,
        "list_tasks": list_tasks
        })

@login_required
def list_categories(request):
    list_categories = Category.objects.filter(user=request.user)
    return render(request, "core/categories.html", {"list_categories": list_categories })

@login_required
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect("list_categories")
        else:
            print(form.errors)
    else:
        form = CategoryForm
    return render(request, "core/new_category.html", {"form": form})

@login_required
def add_task(request):
    if request.method == "POST":
        form = TaskForm(user=request.user, data=request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect("core")
        else:
            print(form.errors)
    else:
        form = TaskForm(user=request.user)
    return render(request, "core/new_task.html", {"form": form})

@login_required
def delete_task(request, id_task):
    task = get_object_or_404(Task, id=id_task)
    if task.user == request.user:
        task.delete()
    else:
        messages.error(request, "You don't have permission!")
        return redirect("core")
    return redirect("core")

@login_required
def delete_category(request, id_category):
    category = get_object_or_404(Category, id=id_category)
    if category.user == request.user:
        category.delete()
    else:
        messages.error(request, "You don't have permission!")
        return redirect("list_categories")
    return redirect("list_categories")

@login_required
def edit_task(request, id_task):
    task = get_object_or_404(Task, id=id_task, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("core")
    else:
        form = TaskForm(instance=task)
    return render(request, "core/new_task.html", {"form": form })

@login_required
def edit_category(request, id_category):
    category = get_object_or_404(Category, id=id_category, user=request.user)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("list_categories")
    else:
        form = CategoryForm(instance=category)
    return render(request, "core/new_category.html", {"form": form })
