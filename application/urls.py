
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('employee/', views.employee_form, name='employee_insert'), # get and post req. for insert operation
    # path('logout/', views.logout_view, name='logout'),
    path('<int:id>/', views.employee_form, name='employee_update'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('list/', views.employee_list, name='employee_list'),


]