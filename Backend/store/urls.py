from django.urls import path, include
from . import views


urlpatterns = [
    path('api/products/', views.get_products),
    path('api/products/<int:pk>/', views.get_product),
    path('api/categories/', views.get_categories),
    # path('api/', include('store.urls')),
    path('api/cart/', views.get_cart),
    path('api/cart/add/', views.add_to_cart),
    path('api/cart/remove/', views.remove_from_cart),
]
