from django.urls import path
from AuthenticationApp.views import *

urlpatterns = [
    path('', singup_view, name='singup'),
    path('sign-in/', singin_view, name='signin'),
    path('home/', home_view, name='home'),
    path('signout/', signout_view, name='signout'),
]
