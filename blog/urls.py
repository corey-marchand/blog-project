from django.urls import path
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    # path('blog/', BlogPageView.as_view(), name='blog'),
    # path('blog_details/<int:pk>', BlogDetailsView.as_view(), name='blog_details')
]