
from django.urls import path
from menu.api.views import (DishDetailAPIView,
                            DishListCreateAPIView,
                            OrderDetailAPIView,
                            OrderListCreateAPIView,
                            TableDetailAPIView,
                            TableListCreateAPIView)

urlpatterns = [
    path('orders/', OrderListCreateAPIView.as_view(),
         name='order-list'),
    path('orders/<int:pk>', OrderDetailAPIView.as_view(),
         name='order-detail'),
    path('tables/', TableListCreateAPIView.as_view(),
         name='table-list'),
    path('tables/<int:pk>', TableDetailAPIView.as_view(),
         name='table-detail'),
    path('dishes/', DishListCreateAPIView.as_view(),
         name='dish-list'),
    path('dishes/<int:pk>', DishDetailAPIView.as_view(),
         name='dish-detail'),
]
