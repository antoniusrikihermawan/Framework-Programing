# warga/api_urls.py
from django.urls import path, include
# from .views import WargaListAPIView, WargaDetailAPIView, PengaduanListAPIView
from .views import WargaViewSet, PengaduanViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'warga', WargaViewSet, basename='warga')
router.register(r'pengaduan', PengaduanViewSet, basename='aduan')

urlpatterns = [
#     path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
#     path('warga/<int:pk>/', WargaDetailAPIView.as_view(), name='api-warga-detail'),
#     path('pengaduan/<int:pk>/', PengaduanListAPIView.as_view(), name='api-warga-detail'),
      path('', include(router.urls)),
 ]
