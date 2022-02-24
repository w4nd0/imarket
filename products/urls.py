from .views import ProductModelViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(prefix=r'products', viewset=ProductModelViewSet)

urlpatterns = router.urls
