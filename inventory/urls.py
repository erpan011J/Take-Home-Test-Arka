from django.urls import path
from .views import product_views, client_views, user_views

urlpatterns = [
    path('users/', user_views.UserListCreateAPIView.as_view(), name='user-list-create'),
    path('login/', user_views.UserLoginAPIView.as_view(), name='user-login'),
    path('users/<int:pk>/', user_views.UserDetailAPIView.as_view(), name='user-detail'),
    path('products/', product_views.ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', product_views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('clients/', client_views.ClientListCreateAPIView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', client_views.ClientDetailAPIView.as_view(), name='client-detail'),
]
