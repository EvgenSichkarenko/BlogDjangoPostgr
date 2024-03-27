from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import F
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from .models import Category, Posts, Tags, Quote, EmailSubs, Comments
from .forms import EmailSubsForm, CommentsForm


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


class CategoryView(View):
    def get(self, request, slug):
        posts = Posts.objects.filter(category__slug=slug)
        quotes = Quote.objects.filter(category__slug=slug)
        category = Category.objects.get(slug=slug)
        try:
            comments = Comments.objects.filter(category__slug=slug)
        except Comments.DoesNotExist:
            comments = None
        context = {
            'posts': posts,
            'quotes': quotes,
            'category': category,
            'comments': comments,
            'form': EmailSubsForm(),
            'form_com': CommentsForm()
        }
        return render(request, 'blog/single.html', context)

    def post(self, request, slug):
        emails = EmailSubs.objects.all()
        posts = Posts.objects.filter(category__slug=slug)
        quotes = Quote.objects.filter(category__slug=slug)
        category = Category.objects.get(slug=slug)

        if request.POST.get('email') not in emails:
            if request.method == 'POST':
                form = EmailSubsForm(request.POST)
                form_com = CommentsForm(request.POST)
                if form.is_valid():
                    form.save()
                elif form_com.is_valid():
                    comment = form_com.save(commit=False)
                    comment.category = category
                    comment.save()
                    mail = send_mail('Subscribe email notification Dartblog',
                                     'Welcome dear friend and thank you for subscribe',
                                     'evgen20@yahoo.com',
                                     [form.cleaned_data.get('email')],
                                     fail_silently=False, )

                    if mail:
                        messages.success(request, 'You are successful subscribe')
                        # return redirect('home')
                    else:
                        messages.error(request, 'Operation is canceled')
                else:
                    messages.error(request, 'Form isn"t valid')
            else:
                messages.error(request, 'You are already subscribed')

        context = {
            'posts': posts,
            'quotes': quotes,
            'category': category,
            'form': EmailSubsForm(),
            'form_com': CommentsForm()
        }

        return render(request, 'blog/single.html', context)


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
