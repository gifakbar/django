from django.urls import path
from . import views



urlpatterns=[
   path('', views.home, name='Home'),
   path('about/', views.about, name='about'),
   path ('kegiatan/', views.todos,name='todos'),
]