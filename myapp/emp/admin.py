from django.contrib import admin

# Register your models here.
from .models import Emp


class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working','phone','emp_id')
    list_editable=('working',)  
    search_fields=('emp_id','name')
    list_filter=('working',) 

admin.site.register(Emp,EmpAdmin) 

