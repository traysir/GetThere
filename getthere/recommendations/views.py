from rest_framework import viewsets
from .models import MediaItem, UserPreference
from .serializers import MediaItemSerializer, UserPreferenceSerializer

class MediaItemViewSet(viewsets.ModelViewSet):
    queryset = MediaItem.objects.all()
    serializer_class = MediaItemSerializer

class UserPreferenceViewSet(viewsets.ModelViewSet):
    queryset = UserPreference.objects.all()
    serializer_class = UserPreferenceSerializer
