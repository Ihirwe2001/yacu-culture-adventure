from django.urls import path
from .views import booking_view, success_view
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('package/', views.package, name='package'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('destination/', views.destination, name='destination'),
    path('guide/', views.guide, name='guide'),
    path('single/', views.single, name='single'),
    path('testmonial/', views.testmonial, name='testmonial'),
    path('booking/', booking_view, name='booking_form'),
    path('success/', success_view, name='success_page'),
]
