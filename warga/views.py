from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm
# from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import WargaSerializer, PengaduanSerializer
from rest_framework import viewsets

#  --- API VIEWS ---
class WargaViewSet(viewsets.ModelViewSet):
     queryset = Warga.objects.all().order_by('-tanggal_registrasi')
     serializer_class = WargaSerializer

class PengaduanViewSet(viewsets.ModelViewSet):
     queryset = Pengaduan.objects.all()
     serializer_class = PengaduanSerializer
     
#  --- API VIEWS ---
# class WargaListAPIView(ListAPIView):
#     queryset = Warga.objects.all()
#     serializer_class = WargaSerializer

# class WargaDetailAPIView(RetrieveAPIView):
#     queryset = Warga.objects.all()
#     serializer_class = WargaSerializer

# class PengaduanListAPIView(ListAPIView):
#     queryset = Pengaduan.objects.all()
#     serializer_class = PengaduanSerializer

class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'


class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'


class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'


class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga:warga-list')  # redirect ke daftar warga setelah tambah


class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('warga:pengaduan_list')  # redirect ke daftar pengaduan


class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'  # pakai template yang sama dengan tambah
    success_url = reverse_lazy('warga:warga-list')  # redirect ke daftar warga setelah update


class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga:warga-list')  # redirect ke daftar warga setelah hapus

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('warga:pengaduan_list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('warga:pengaduan_list')
