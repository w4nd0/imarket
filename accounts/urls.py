from django.urls import path

from accounts.views import UserView, UserDetailView, LoginUserView


urlpatterns = [
    path('accounts/', UserView.as_view()),
    path('accounts/<int:pk>/', UserDetailView.as_view()),

    path("login/", LoginUserView.as_view()),
]

# urlpatterns += router.urls
