from django.urls import path

from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.home, name="home"),
    path('contact_us/', views.contact_view, name="contact"),
    path('track_shipment/', views.track_shipment, name="track_shipment"),
    path('about/', views.about, name="about"),

    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]