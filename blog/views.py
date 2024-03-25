from django.db.models import F
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Category, Posts, Tags, Quote


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
        context['quotes'] = Quote.objects.filter(category__slug=self.kwargs['slug'])
        return context


class PostsViews(View):

    def get(self, request, slug):
        post = Posts.objects.get(slug=slug)
        post.views = F('views') + 1
        post.save()
        post.refresh_from_db()

        context = {
            'post': post
        }

        return render(request, 'blog/post.html', context)


class TagsViews(ListView):
    template_name = 'blog/tags.html'
    model = Posts
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Posts.objects.filter(tags__slug=self.kwargs['slug'])


class SearchView(ListView):
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        value = self.request.GET.get('s')
        if value:
            return Posts.objects.filter(title__icontains=value)
        else:
            return []

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f's={self.request.GET.get("s")}&'
        return context
