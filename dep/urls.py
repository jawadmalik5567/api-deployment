from django.urls import path
from .views import AddNumbersAPIView

urlpatterns = [
    path('add/', AddNumbersAPIView.as_view(), name='add-numbers'),
]
