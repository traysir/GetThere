from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # This is for the Django admin panel
    path('api/', include('recommendations.urls')),  # Includes the URLs from the recommendations app
]
