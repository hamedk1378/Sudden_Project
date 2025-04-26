from django.urls import path

from .views import BlogsHomeView


urlpatterns= [
        path("", BlogsHomeView, name="blogs_home"),

        ]


