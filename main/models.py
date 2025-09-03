from django.db import models

class VardiyaCizelgesi(models.Model):
    ay = models.IntegerField()
    yil = models.IntegerField()
    veri = models.JSONField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ay}-{self.yil} Vardiya Çizelgesi"

    class Meta:
        unique_together = ('ay', 'yil')

class Arac(models.Model):
    isim = models.CharField(max_length=100)
    plaka = models.CharField(max_length=20, unique=True)
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.isim} ({self.plaka})"

class AracTakip(models.Model):
    arac = models.ForeignKey(Arac, on_delete=models.CASCADE, related_name='takipler')
    personel = models.CharField(max_length=100)
    durum = models.CharField(max_length=20)  # 'aldim' veya 'teslim'
    zaman = models.DateTimeField(auto_now_add=True)
    yorum = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.arac} - {self.personel} - {self.durum}"
