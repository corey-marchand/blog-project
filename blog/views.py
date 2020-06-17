from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .models import Blog

# Create your views here.

class BlogListView(ListView):
    template_name = 'base.html'
    model = Blog

class BlogDetailView(DetailView):
    template_name = 'blog_details.html'
    model = Blog

class BlogCreateView(CreateView):
    template_name = 'blog_create.html'
    model = Blog
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    template_name = 'blog_update.html'
    model = Blog
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    template_name = 'blog_delete.html'
    model = Blog
    success_url = reverse_lazy('blog_list')
