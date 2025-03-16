from django.contrib import admin
from . import models
# Register your models here.



from django.contrib import admin
from . import models

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'course', 'institute', 'address', 'photo') 
    search_fields = ('first_name', 'last_name', 'email', 'phone')  
    list_filter = ('course', 'institute')  
    ordering = ('first_name',)  

admin.site.register(models.Student, StudentAdmin)