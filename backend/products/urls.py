from django.urls import path
from .views import ProductDetailAPIView, product_list_create_view

urlpatterns = [
    path('', product_list_create_view),
    path('<int:pk>/', ProductDetailAPIView.as_view())

]
