from django.urls import path
from StudentApp.views import *

urlpatterns = [
    path('', std_view, name='std'),
    path('addstd/', add_std_view, name='add_std'),
    path('editstd/<str:eid>/', edit_std_view, name='edit_std'),
    path('delstd/<str:eid>/', delete_std_view, name='delete_std'),
]