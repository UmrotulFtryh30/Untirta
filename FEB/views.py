from django.shortcuts import render

# Create your views here.
def prodi2(request):
    judul = ["Program Sarjana Managemen", "Program Sarjana Akuntansi", "Program Sarjana Ilmu Ekonomi Pembangunan", "Program Sarjana Ekonomi Syariah", "Diploma III Akuntansi", "Diploma III Marketing", "Diploma III Perpajakan", "Diploma III Keuangan Perbankan"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexfeb.html', konteks)
