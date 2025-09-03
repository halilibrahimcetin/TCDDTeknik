from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vardiya/', views.vardiya, name='vardiya'),

    # Araç sayfası
    path('arabalar/', views.arac_takip_view, name='arabalar'),
    
    # API URL'leri
    path('api/arac-takip/', views.arac_takip_api, name='api_arac_takip'),
    path('api/arac-durumu/', views.arac_durumu, name='api_arac_durumu'),

    # Vardiya çizelgesi API
    path('api/save_schedule/', views.kaydet_cizelge, name='kaydet_cizelge'),
    path('api/load_schedule/', views.yukle_cizelge, name='yukle_cizelge'),
    path('api/export_schedule_excel/', views.export_cizelge_excel, name='export_cizelge_excel'),
]
