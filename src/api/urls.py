from django.urls import path, include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", BookViewSet, basename="")

urlpatterns = [
    path("", include(router.urls)),
    path("<int:id>", include(router.urls)),
]
