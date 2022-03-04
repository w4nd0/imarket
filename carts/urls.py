# from django.urls import path

# from carts.views import CartDetailViewSet, CartListViewSet
from carts.views import CartUpdateRetrieveView
from rest_framework.routers import SimpleRouter
from django.urls import path

# urlpatterns = [
#     path('cart/', CartListViewSet.as_view()),
#     path('cart/<int:pk>/', CartDetailViewSet.as_view()),
# ]
urlpatterns = [
    path('carts/', CartUpdateRetrieveView.as_view({'get': 'retrieve', 'patch': 'update'})),
    # path('students/<int:pk>/', StudentViewSet.as_view({'get': 'retrieve'})),
]

# router = SimpleRouter()
# router.register(prefix=r'carts', viewset=CartUpdateRetrieveView)


# urlpatterns = router.urls
