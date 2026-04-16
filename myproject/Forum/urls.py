from django.urls import path
from . import views

urlpatterns = [
    path("", views.forum, name="forum"),
    path("new_post/", views.create_post, name="new_post"),

    path("delete/<int:post_id>/", views.delete_post, name="delete_post"),
    path("post/<int:post_id>/edit/", views.edit_post, name="edit_post"),

]
