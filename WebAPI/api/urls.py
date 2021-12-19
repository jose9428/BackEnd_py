from django.urls import path
from .views import CategoriaView


urlpatterns = [
    path('categorias/' , CategoriaView.as_view()),
    path('categorias/<int:id>' , CategoriaView.as_view())
]