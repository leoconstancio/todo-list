from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path(r'create-account/', views.add_user, name='add_user'),
    path(r'change-password/', views.change_password, name='change_password'),
    path(r'login/', views.user_login, name='user_login'),
    path(r'logout/', views.user_logout, name='user_logout'),

]
