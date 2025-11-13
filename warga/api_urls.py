# warga/api_urls.py
from django.urls import path, include
from .views import WargaListAPIView, WargaDetailAPIView, PengaduanListAPIView

urlpatterns = [
    path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
    path('warga/<int:pk>/', WargaDetailAPIView.as_view(), name='api-warga-detail'),
    path('pengaduan/<int:pk>/', PengaduanListAPIView.as_view(), name='api-warga-detail'),
]
