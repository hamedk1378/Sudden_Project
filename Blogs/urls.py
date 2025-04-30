from django.urls import path

from . import views

app_name = "blogs"
urlpatterns= [
        path("", views.IdeasIndexView.as_view(), name="idea_index"),
        path("<int:pk>/", views.IdeaDetailView.as_view(), name="idea_detail"),
        path("<int:idea_id>/like_idea/", views.like_idea_view, name="like_idea"),
        ]


