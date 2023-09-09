from django.urls import path
from . import views


urlpatterns = [
    path('apartment/<int:object_id>/', views.Apartment_view.as_view(), name='show_object'),
]