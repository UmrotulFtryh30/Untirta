from django.shortcuts import render

# Create your views here.
def prodi6(request):
    judul = ["Pendidikan Matematika", "Pendidikan Nonformal", "Pendidikan IPA", "Pendidikan Bahasa Inggris", "Pendidikan Bahasa Indonesia", "Pendidikan Biologi", "Pendidikan Guru Sekolah Dasar", "Pendidikan Guru PAUD", "Pendidikan Bimbingan Dan Konseling", "Pendidikan Fisika", "Pendidikan Kimia", "Pendidikan Khusus", "Pendidikan PKN", "Pendidikan Sosiologi", "Pendidikan Sejarah", "Pendidikan Seni Dan Pertunjukan", "Pendidikan Vokasional Teknik Elektro", "Pendidikan Vokasional Teknik Mesin"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexfkip.html', konteks)
