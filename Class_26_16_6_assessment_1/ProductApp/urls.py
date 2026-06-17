from django.urls import path
from ProductApp.views import *

urlpatterns = [
    path('', prd_view, name='prd'),
    path('addprd/', add_prd_view, name='add_prd'),
    path('editprd/<str:eid>/', edit_prd_view, name='edit_prd'),
    path('delprd/<str:eid>/', delete_prd_view, name='delete_prd'),
]