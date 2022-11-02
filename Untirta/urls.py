"""Untirta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from FAPERTA.views import prodi1
from FEB.views import prodi2
from FH.views import prodi3
from FISIP.views import prodi4
from FK.views import prodi5
from FKIP.views import prodi6
from FT.views import prodi7
from pascasarjana.views import prodi8
from profil.views import profil
from universitas.views import universitas
from dosen.views import dosen
from mahasiswa.views import mahasiswa
from tendik.views import tendik
from mahasiswa.views import tambah_mahasiswa
from dosen.views import tambah_dosen
from tendik.views import tambah_tendik
from mahasiswa.views import ubah_mahasiswa
from mahasiswa.views import hapus_mahasiswa
from dosen.views import ubah_dosen
from dosen.views import hapus_dosen
from tendik.views import ubah_tendik
from tendik.views import hapus_tendik






urlpatterns = [
    path('admin/', admin.site.urls),
    path('FAPERTA', prodi1,name="FAPERTA"),
    path('FEB', prodi2,name="FEB"),
    path('FH', prodi3,name="FH"),
    path('FISIP', prodi4,name="FISIP"),
    path('FK', prodi5,name="FK"),
    path('FKIP', prodi6,name="FKIP"),
    path('FT', prodi7,name="FT"),
    path('pascasarjana/', prodi8,),
    path('profil/', profil),
    path('universitas/', universitas),
    path('dosen/', dosen),
    path('mahasiswa/', mahasiswa),
    path('tendik/', tendik),
    path('tambah-mahasiswa/', tambah_mahasiswa),
    path('tambah-dosen/', tambah_dosen),
    path('tambah-tendik/', tambah_tendik),
    path('mahasiswa/ubah/<int:id_mahasiswa>', ubah_mahasiswa, name='ubah_mahasiswa'),
    path('mahasiswa/hapus/<int:id_mahasiswa>', hapus_mahasiswa, name='hapus_mahasiswa'),
    path('dosen/ubah/<int:id_dosen>', ubah_dosen, name='ubah_dosen'),
    path('dosen/hapus/<int:id_dosen>', hapus_dosen, name='hapus_dosen'),
    path('tendik/ubah/<int:id_tendik>', ubah_tendik, name='ubah_tendik'),
    path('tendik/hapus/<int:id_tendik>', hapus_tendik, name='hapus_tendik'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
