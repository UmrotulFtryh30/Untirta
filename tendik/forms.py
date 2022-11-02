from tkinter import Widget
from django.forms import ModelForm 
from tendik.models import Tendik
from django import forms 

class FormTendik(ModelForm):
    class Meta:
        model = Tendik
        fields = '__all__'