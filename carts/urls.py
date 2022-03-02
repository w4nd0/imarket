from django.urls import path

from carts.views import CartDetailViewSet, CartListViewSet

urlpatterns = [
    path('cart/', CartListViewSet.as_view()),
    path('cart/<int:pk>/', CartDetailViewSet.as_view()),
]
