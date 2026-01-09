from django.urls import path, include
from . import views


urlpatterns = [
    path('api/products/', views.get_products),
    path('api/products/<int:pk>/', views.get_product),
    path('categories/', views.get_categories),
    # path('api/', include('store.urls')),

]
