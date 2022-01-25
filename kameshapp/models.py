from django.db import models

# Create your models here.
class kameshmodel(models.Model) :
    stdname=models.CharField(max_length=30)
    stdrollno=models.IntegerField(default=0)
    stdemail=models.EmailField()
    stdmobile=models.IntegerField(default=0)
    stdaddress=models.CharField(max_length=30)
    stdqualification=models.CharField(max_length=30)

