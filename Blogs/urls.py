from django.urls import path

from . import views

app_name = "blogs"
urlpatterns= [
        path("", views.blogs_home_view, name="blogs_home"),
        path("index/", views.ideas_index_view, name="idea_index"),
        path("<int:idea_id>/", views.idea_detail_view, name="idea_detail"),
        ]


