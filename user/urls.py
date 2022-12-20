from . views import *
from django.urls import path

urlpatterns = [
    path('signup/',signup,name="signup"),
    path('login/',login,name="login"),
    path('index/',index,name="index")
]