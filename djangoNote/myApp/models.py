from django.db import models

# Create your models here.

class myManager(models.Manager):
   def get_queryset(self):
    return super(myManager,self).get_queryset().filter(fSingle=True)


class myFriend(models.Model):
    manager=myManager()

    fName = models.CharField(max_length=20)
    fSex = models.BooleanField(default=True)
    fAge = models.IntegerField()
    fSingle = models.BooleanField(default=True)
    class Meta:
        db_table="myFriend"
        ordering=["id"]



