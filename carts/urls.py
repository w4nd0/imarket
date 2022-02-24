from .views import CartModelViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(prefix=r'carts', viewset=CartModelViewSet)

urlpatterns = router.urls
