from os import name
from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [

    path('student-login/',views.StudentLogin,name='student-login'),
    path('student-checklogin',views.CheckStudentLogin,name='student-checklogin'),
    path('studentlogout/',views.Logout),
    path('student-dashboard/',views.Studentdashboard,name='student-dashboard'),
    path('student-register/',views.Registeration,name='student-register'),
    path('student-buysell/',views.BuySell,name='student-buysell'),
    path('product-submit/',views.Productsubmit,name='product-submit'),
    path('chat/<int:id>',views.Chat,name='chat'),

    path('activate/<uidb64>/<token>',
         views.ActivateAccountView.as_view(), name='activate'),
]