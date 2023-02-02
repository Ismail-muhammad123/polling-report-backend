from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # api urls
    path('api/auth/', include('rest_framework.urls')),  # for authentication
    path('api/reports/', include('reports.api_urls')),  # for repost
]
