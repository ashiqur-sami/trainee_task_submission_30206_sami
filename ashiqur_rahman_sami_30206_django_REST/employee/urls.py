from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.get_employees, name='get_employees'),
    path('employees/create/', views.create_employee, name='create_employee'),
    path('employees/<int:pk>/', views.get_employee, name='get_employee'),
    path('employees/<int:pk>/update/', views.update_employee, name='update_employee'),
    path('employees/<int:pk>/delete/', views.delete_employee, name='delete_employee'),
]
