from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView

from blog.models import Blog


# Create your views here.

class BlogListView(ListView):

    model = Blog


class BlogDetailView(DetailView):

    model = Blog

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def get_object(self, queryset=None):

        self.object = super().get_object()
        self.object.count_views += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):

    model = Blog
    fields = ('article_title', 'is_published', 'article_body', 'article_image', 'publicated_date', 'count_views')
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(UpdateView):

    model = Blog
    fields = ('article_title', 'is_published', 'article_body', 'article_image')
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):

        if form.is_valid():
            new_mat = form.save()
            new_mat.save()
        return super().form_valid(form)


class BlogDeleteView(DeleteView):

    model = Blog
    success_url = reverse_lazy('blog:blog_list')
