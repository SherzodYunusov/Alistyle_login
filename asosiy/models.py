from django.db import models

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
    matn = models.TextField()
    kafolat = models.CharField(max_length=50)
    chegirma = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.nom

class Media(models.Model):
    rasm = models.FileField(upload_to='mahsulot')
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)

# Create your models here.
