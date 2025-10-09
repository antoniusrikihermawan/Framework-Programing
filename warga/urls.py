from django.urls import path
from .views import WargaListView, PengaduanListView

urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan_list'),
]
