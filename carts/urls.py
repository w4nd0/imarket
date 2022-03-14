from django.urls import path
# from django.conf.urls import include, urls   

# from carts.views import CartDetailViewSet, CartListViewSet
# from carts.views import ReadCartView, UpdateCartView
# from rest_framework.routers import SimpleRouter
# from django.urls import path
from rest_framework import routers

from carts.views import ReadCartView, UpdateCartView


# urlpatterns = [
#     path('cart/', CartListViewSet.as_view()),
#     path('cart/<int:pk>/', CartDetailViewSet.as_view()),
# ]
router = routers.SimpleRouter()
# urlpatterns = [
#     path('buy/', UpdateCartView.as_view({'patch':'update'})),
#     # path('carts/<int:pk>/', ReadCartView.as_view()),
# ]

urlpatterns = [
    path('cart/', UpdateCartView.as_view({'patch': 'update'})),
]

# router = SimpleRouter()
# router.register(prefix=r'carts', viewset=CartUpdateRetrieveView)


# router.register(r"buy", UpdateCartView, name='buy')
router.register(r"cart", ReadCartView)

# urlpatterns = [
#    url(r'^', include(router.urls)),
# ]
urlpatterns += router.urls

