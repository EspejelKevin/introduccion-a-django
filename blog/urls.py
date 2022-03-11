from django.urls import path
from .views import BlogCreateView, BlogDeleteView, BlogEditView, BlogListView

app_name="blog"

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("create/", BlogCreateView.as_view(), name="create"),
    path("edit/<int:id>", BlogEditView.as_view(), name="edit"),
    path("delete/<int:id>", BlogDeleteView.as_view(), name="delete")
]