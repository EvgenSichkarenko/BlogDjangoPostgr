from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Posts, Tags


# Create your views here.
class Home(ListView):
    template_name = 'blog/index.html'
    model = Posts
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'CLASSIC BLOG DESIGN'
        return context


class CategoryView(DetailView):
    template_name = 'blog/single.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Posts.objects.filter(category__slug=self.kwargs['slug'])
        context['tags'] = Tags.objects.all()
        return context


class PostsViews(DetailView):
    template_name = 'blog/post.html'
    model = Posts
    context_object_name = 'post'
