from django.urls import path
from . views import *

urlpatterns = [
    path('',register,name='register'),
    path('student_login',student_login,name='student_login'),
    path('staff_login',staff_login,name='staff_login'),
    path('admin_login',admin_login,name='admin_login'),
    path('editor_login',editor_login,name='editor_login'),
    path('logout',student_logout,name='student_logout')
]