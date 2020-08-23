from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogPostsIndex, name="blogPostsIndex"),
    path("<int:pk>/", views.blogPostDetails, name="blogPostDetails"),
    path("<category>/", views.blogPostsCategory, name="blogPostsCategory"),
]
