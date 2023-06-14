from django.db import models
from userapp.models import Account
class Bolim(models.Model):
    nom = models.CharField(max_length=50)
    rasm = models.FileField(upload_to='bolimlar')
    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    narx = models.PositiveSmallIntegerField()
    min_miqdor = models.PositiveSmallIntegerField(default=1)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)
    davlat = models.CharField(max_length=60)
    brend = models.CharField(max_length=60)
    yetkazish = models.CharField(max_length=60)
    mavjud = models.BooleanField(default=True)
    matn = models.TextField()
    kafolat = models.CharField(max_length=50)
    chegirma = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.nom

class Media(models.Model):
    rasm = models.FileField(upload_to='mahsulot')
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)


class Izoh(models.Model):

    matn = models.TextField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    sana = models.DateField()
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    baho = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.matn
# Create your models here.
