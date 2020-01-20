from django.urls import path
from . import views

urlpatterns = [
    path('<str:datatype>/<int:item_id>/', views.show),
    path('', views.index)
]