from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MediaItemViewSet, UserPreferenceViewSet

router = DefaultRouter()
router.register(r'media-items', MediaItemViewSet)
router.register(r'user-preferences', UserPreferenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
