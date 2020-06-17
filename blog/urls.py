from django.urls import path
from .views import BlogListView, BlogDeleteView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name="blog_list"),
    path('blog/new', BlogCreateView.as_view(), name="blog_create"),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name="blog_delete"),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name="blog_details"),
    path('blog/<int:pk>/edit', BlogUpdateView.as_view(), name="blog_update"),
]
