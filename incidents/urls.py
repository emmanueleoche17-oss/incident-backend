from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, IncidentViewSet, LoginView, RegisterView

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="category")
router.register("incidents", IncidentViewSet, basename="incident")

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("", include(router.urls)),
]
