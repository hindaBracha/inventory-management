from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_category/', views.add_category, name='add_category'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('api/chat', views.chat_api, name='chat_api'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
