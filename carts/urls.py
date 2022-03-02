# from django.urls import path

# from carts.views import CartDetailViewSet, CartListViewSet
from carts.views import CartCreateListRetrieveView
from rest_framework.routers import SimpleRouter

# urlpatterns = [
#     path('cart/', CartListViewSet.as_view()),
#     path('cart/<int:pk>/', CartDetailViewSet.as_view()),
# ]
router = SimpleRouter()
router.register('carts', CartCreateListRetrieveView, basename='carts')

urlpatterns = router.urls
