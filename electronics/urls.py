from django.urls import path
from electronics import views

urlpatterns = [
    path('', views.home, name="home")
]
