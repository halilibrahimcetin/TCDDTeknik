from django.contrib import admin
from .models import VardiyaCizelgesi, Arac, AracTakip

admin.site.register(VardiyaCizelgesi)

@admin.register(Arac)
class AracAdmin(admin.ModelAdmin):
    list_display = ("isim", "plaka", "aktif")
    search_fields = ("isim", "plaka")

@admin.register(AracTakip)
class AracTakipAdmin(admin.ModelAdmin):
    list_display = ("arac", "personel", "durum", "zaman")
    search_fields = ("arac__isim", "arac__plaka", "personel")
    list_filter = ("durum", "zaman")
