from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    
    path("manish",views.manish,name="manish"),
    path("David",views.David,name="David"),
    path("<str:name>",views.greet,name="greet")
]