"""
Api Url BaseConfiguration
"""
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

BASE_API_URL = "api/v1"

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"{BASE_API_URL}/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        f"{BASE_API_URL}/swagger/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="swagger-ui",
    ),
]
