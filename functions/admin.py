from django.contrib import admin
from .models import Diary
# Register your models here.

class Hide_content(admin.ModelAdmin):
	exclude= ['content']
	list_display= ['user','title']


admin.site.register(Diary, Hide_content)
