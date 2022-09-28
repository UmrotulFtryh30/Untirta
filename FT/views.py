from django.shortcuts import render

# Create your views here.
def prodi7(request):
    judul = ["Teknik Elektro", "Teknik Kimia", "Teknik Industri", "Teknik Metalurgi", "Teknik Sipil", "Teknik Mesin"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexft.html', konteks)