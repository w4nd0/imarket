from .views import PurchaseListCreateView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(prefix=r'shop', viewset=PurchaseListCreateView)

urlpatterns = router.urls
