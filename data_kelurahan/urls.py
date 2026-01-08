from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
# Impor baru
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('warga/', include('warga.urls')), 
    path('api/', include('warga.api_urls')),# URL untuk web
    path('api/auth/token/', obtain_auth_token, name='api-token-auth'),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),

    # --- URL DOKUMENTASI API ---
    # Menghasilkan file schema.yml
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Halaman Swagger UI
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Halaman Redoc
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
