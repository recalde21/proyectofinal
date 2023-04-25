from django import forms
from .models import Blog

class PageCreationForm(forms.ModelForm):
    titulo = forms.CharField(
        label='Título*',
        widget=forms.TextInput(attrs={
            "class":"form-control",
            #"id":"nombre_rep",
            #"readonly":"readonly",
            #"disabled":"disabled",
        })
    )
    subtitulo = forms.CharField(
        label='Subtítulo*',
        widget=forms.TextInput(attrs={
            "class":"form-control",
            #"id":"nombre_rep",
            #"readonly":"readonly",
            #"disabled":"disabled",
        })
    )
    cuerpo = forms.CharField(
        label='Cuerpo*',
        widget=forms.TextInput(attrs={
            "class":"form-control",
            #"id":"nombre_rep",
            #"readonly":"readonly",
            #"disabled":"disabled",
        })
    )
    imagen = forms.ImageField(
        label='Imagen*',
        required=False,
        widget=forms.FileInput(attrs={
            "class":"form-control",
        })
    )

    class Meta:
        # To specify the model to be used to create form
        model = Blog
        # It includes all the fields of model
        #fields = '__all__'
        fields = [
            'titulo',
            'subtitulo',
            'cuerpo',
            'imagen'
        ]
