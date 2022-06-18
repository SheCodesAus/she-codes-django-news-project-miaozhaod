from django.urls import path, re_path
from . import views

app_name = "news"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.StoryView.as_view(), name="story"),
    path("add-story/", views.AddStoryView.as_view(), name="newStory"),
    path("stories-order-by-date/", views.storiesByDateView.as_view(), name="storiedByDate"),
    re_path(r'^author/(?P<author>\d+)$', views.storiesByAuthorView.as_view(), name='storiesByAuthor'),
    # path("authors/<int:author_id>/", views.storiesByAuthorView.as_view(), name="storiesByAuthor"),
]
