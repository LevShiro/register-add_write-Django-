from .models import Articles
from django.forms import ModelForm,TextInput,Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ["title","anons","full_text",'autor']

        widgets = {
            "title": TextInput(attrs = {
                'class':'form-control',
                'placeholder':'Название записи'
            }),
            "anons": TextInput(attrs = {
                'class':'form-control',
                'placeholder':'Анонс'
            }),
            "full_text": Textarea(attrs = {
                'class':'form-control',
                'placeholder':'Текст записи'
            })
        }