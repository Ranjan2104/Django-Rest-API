from . import views
from django.urls import path

urlpatterns = [
    path('api/v1/getApi/', views.getApi),
    path('api/v1/postApi/', views.postApi),
    path('api/v1/deleteApi/', views.deleteApi),
]