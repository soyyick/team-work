from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexPage, name= 'index'),
<<<<<<< HEAD
    path('continue/', views.continue_view, name='continue'),
=======
    path("login/", views.loginPage, name= 'login'),
    path("map/", views.mappage, name= 'map'),
<<<<<<< HEAD
>>>>>>> e09930b19ee8f0f38869578d4db7dbdeecd94b04
=======
>>>>>>> 051f978eebb86c8e562d3a434c2673e9d07c8899
]
