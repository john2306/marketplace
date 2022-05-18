from django.urls import path
from .views import (
                    ProductosApiView, 
                    ProductoCreateApiView, 
                    CategoriaApiView, 
                    ProductoRetrieveApiView,
                    ProductoDestroyApiView, 
                    ProductoUpdateApiView,
                    CategoriaProductosView,
                    CategoriaUpdateApiView,
                    CategoriaDestroyApiView
                    )  

urlpatterns = [
    path('', ProductosApiView.as_view()),
    path('<int:pk>/', ProductoRetrieveApiView.as_view()),
    path('create/', ProductoCreateApiView.as_view()),
    path('delete/<int:pk>/', ProductoDestroyApiView.as_view()),
    path('update/<int:pk>/', ProductoUpdateApiView.as_view()),

    # Categorias CRUD API
    path('categorias/', CategoriaApiView.as_view()), # Listado de categorias 
    path('categoria/<int:categoria>/productos/', CategoriaProductosView.as_view()), # Listado de productos por categoria 
    path('categoria/<int:pk>/editar/', CategoriaUpdateApiView.as_view()), # Editar categoria
    path('categoria/<int:pk>/eliminar/', CategoriaDestroyApiView.as_view()), # Eliminar de categoria

]