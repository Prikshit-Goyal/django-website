from django.contrib import admin
from django.urls import include, path
from home import views

urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('services',views.services, name='services'),
    path('contact',views.contact, name='contact'),
    path('save_contact',views.save_contact, name='save_contact'),
    path('login',views.loginfunc, name='login'),
    path('loginuser',views.loginuser, name='loginuser'),
    path('logout',views.logoutfunc, name='logout'),

    path('textutils',views.textutils, name='textutils'),
    path('result',views.result, name='result'),
    path('capataliizefirst',views.capataliizefirst, name='capataliizefirst'),
    path('spaceremove',views.spaceremove, name='spaceremove'),
    path('charcount',views.charcount, name='charcount'),
]
