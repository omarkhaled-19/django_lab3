from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('landing',views.landingpage,name='landing'),
    path('index',views.productspage,name='products'),
    path('test_layout',views.test_layout,name='test_layout'),
    path('all',views.all_products,name='products_db'),
    path('show/<int:product_id>',views.show_product,name='products.show'),
    path('delete/<int:product_id>',views.delete_product,name='products.delete'),
    path('create',views.create_product,name='products.create')
]