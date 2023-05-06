from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:clothing_item_id>/', views.clothing_item_detail, name='outlet_item'),
]
