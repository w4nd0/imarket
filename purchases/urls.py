from .views import PurchaseListCreateView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(prefix=r'shops', viewset=PurchaseListCreateView)

urlpatterns = router.urls
