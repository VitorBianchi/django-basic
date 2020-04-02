from django.urls import path
from .views import index, product


urlpatterns = [
    path('', index, name="index"),
    path('product/<int:id>', product, name="product")
]
