from django.forms import ModelForm
from .models import Diary

class Content_field(ModelForm):
	class Meta:
		model=Diary
		fields=['title','content']