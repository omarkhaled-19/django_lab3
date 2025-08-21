from django.urls import path
from . import views

urlpatterns = [
    path('contact',views.contactuspage,name='contactus')
]