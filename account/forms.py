from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('category', 'detail_text', 'detail_img', 'prev_text', 'slug', 'name', 'prev_img')
        widgets = {
            'detail_text': SummernoteWidget(),
            'prev_text': SummernoteWidget(),

        }

class CreateSliderForm(forms.ModelForm):
    class Meta:
        model = MainSlider
        fields = ('name', 'img', 'href')
