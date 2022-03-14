from django.urls import path,include
from duf import views

urlpatterns = [
    path('',views.index),
    path('uploadFile',views.uploadFile)
]