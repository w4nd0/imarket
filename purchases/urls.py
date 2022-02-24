from .views import PurchaseModelViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(prefix=r'purchase', viewset=PurchaseModelViewSet)

urlpatterns = router.urls
