from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView)
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm

class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'  # opsional

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
    success_url = reverse_lazy('warga:warga-list')  # Arahkan ke daftar pengaduan setelah berhasil menambah warga

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    
    # 3. Tentukan ke mana harus pergi setelah form berhasil disimpan
    success_url = reverse_lazy('warga:pengaduan_list')