
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register),
    path('',views.home),
    path('login/',views.login),
    path('studenthome/',views.studenthome)
]
