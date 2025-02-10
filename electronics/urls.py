from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('car/update/<int:car_id>/', views.update_car, name='update_car'),
    path('car/delete/<int:car_id>/', views.delete_car, name='delete_car'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
