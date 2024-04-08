from django.template.backends import django
from django.urls import path, re_path
from . import views
import django.views as my_app

urlpatterns = [
    path('artwork/<str:artwork>/', views.artwork_detail, name='artwork_detail'),
    path('', django.index, name="main_url"), #  my_app = http://127.0.0.1:8000/my_app/
    path('petGET/', django.petGET),  # http://127.0.0.1:8000/pets/petGET/
    path('<slug:pet_slug>/', django.pet), # http://127.0.0.1:8000/pets/{pet_slug}/
    path('categories/<int:categorie_id>/', django.categories), # http://127.0.0.1:8000/pets/categories/{int}/

]
