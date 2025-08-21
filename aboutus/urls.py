from django.urls import path
from . import views

urlpatterns = [
    path('about',views.aboutuspage,name="aboutus")
]