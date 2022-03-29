from .views import CreatePurchaseView, PurchaseListView
from rest_framework.routers import SimpleRouter
from django.urls import path


router = SimpleRouter()

router.register(prefix=r'shop', viewset=PurchaseListView)

urlpatterns = [
    path('shop', CreatePurchaseView.as_view()),
]

urlpatterns += router.urls
