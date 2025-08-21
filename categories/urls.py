from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_category, name='category.create'),
    path('all', views.list_all_categories, name='category.all'),
    path('delete/<int:category_id>',views.delete_category,name='category.delete'),
    path('edit/<int:category_id>',views.edit_category, name= 'category.edit'),
    path('<int:id>', views.show, name='category.show')
]