from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name='home'),
    path('daf/', views.Daf, name='daf'),
    path('iveco/', views.Iveco, name='iveco'),
    path('man/', views.Man, name='man'),
    path('mecerdes/', views.Mercedes, name='mecerdes'),
    path('renalt/', views.Renault, name='renalt'),
    path('scania/', views.Scania, name='scania'),
    path('volvo/', views.Volvo, name='volvo'),
    path('contact/', views.contact_view, name='contact_view'),
    path('thank-you/', views.thank_you, name='thank_you'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
