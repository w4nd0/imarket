from .views import ProductModelViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(prefix=r'product', viewset=ProductModelViewSet)

urlpatterns = router.urls
