from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.main_content,name="home"),
    path("about",views.about_content,name="about"),
    path("contacts",views.contacts_content,name="contacts")
]