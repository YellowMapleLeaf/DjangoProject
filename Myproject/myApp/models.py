from django.db import models

# Create your models here.
class Friends(models.Model):
    fName=models.CharField(max_length=20)
    fSex=models.BooleanField(default=True)
    fAge=models.IntegerField()
    fSingle=models.BooleanField(default=True)


from tinymce.models import HTMLField
class Text(models.Model):
    str=HTMLField()