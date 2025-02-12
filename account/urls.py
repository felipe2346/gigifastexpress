from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('create_shipment/', views.create_new_shipment, name='create_shipment'),
    path('edit_shipment/<pk>/', views.edit_shipment, name='edit_shipment'),
    path('shipment_details/<pk>/', views.shipment_detail, name='shipment_detail'),
    path('delete_shipment/<pk>/', views.delete_shipment, name='delete_shipment'),

    path('update_live_update/<pk>/', views.update_live_update, name='update_live_update'),
    path('delete_live_update/<pk>/', views.delete_live_update, name='delete_live_update'),
    path('view_receipt/<pk>/', views.view_receipt, name='view_receipt'),
]
