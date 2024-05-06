from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogDetailView, BlogCreateView, BlogListView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blog/<int:pk>', cache_page(60)(BlogDetailView.as_view()), name='blog_detail'),
    path('blog/create', BlogCreateView.as_view(), name='create_blog'),
    path('blog_list', BlogListView.as_view(), name='blog_list'),
    path('blog/update/<int:pk>', BlogUpdateView.as_view(), name='update_blog'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='delete_blog'),

]
