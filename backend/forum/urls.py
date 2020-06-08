from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:forum_id>", views.forum, name="forum")
]
