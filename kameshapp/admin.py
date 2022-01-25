from django.contrib import admin
from .models import kameshmodel

# Register your models here.
class kameshadmin(admin.ModelAdmin):
    list_display=["stdname","stdrollno","stdemail","stdmobile","stdaddress","stdqualification"]


admin.site.register(kameshmodel,kameshadmin)







