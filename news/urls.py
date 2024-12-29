from django.urls import path,include

from . import views

urlpatterns = [
    path("",views.news_home, name="news"),
    path("<int:news_id>",views.view_news,name="view_news"),
    path("add_news",views.add_news,name="add_news")
]