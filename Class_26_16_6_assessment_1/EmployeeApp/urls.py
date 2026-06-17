from django.urls import path
from EmployeeApp.views import *

urlpatterns = [
    path('', emp_view, name='emp'),
    path('addemp/', add_emp_view, name='add_emp'),
    path('editemp/<str:eid>/', edit_emp_view, name='edit_emp'),
    path('delemp/<str:eid>/', delete_emp_view, name='delete_emp'),
]