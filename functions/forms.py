from django.forms import ModelForm
from .models import Diary
from django import forms

class Content_field(forms.ModelForm):
	class Meta:
		model=Diary
		fields=['title','content']


		widgets={
			'title': forms.TextInput(attrs={'class': 'textinputclass'}),
			'content' : forms.Textarea(attrs={'class': 'editable medium-editor-textarea '})
		}