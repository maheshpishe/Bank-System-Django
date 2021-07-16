from django.contrib import admin
from django.urls import path,include
from empcrud import views

urlpatterns = [
    path('',views.home,name='home'),
    path('account',views.accnt,name='account'),
    path('transaction',views.transview,name='transview'),
    path('trans',views.trans,name='trans'),
    path('history',views.history,name='history')

    
]