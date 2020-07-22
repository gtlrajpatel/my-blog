from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView

from .models import Blog
from .filters import BlogFilter

import django_filters


class BlogListView(ListView):
    model = Blog
    template_name = 'index.html'
    context_object_name = 'blog_entries'
    paginate_by = 3

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-date')
        return ordering


def search(request):
    blog_list = Blog.objects.all()
    blog_filter = BlogFilter(request.GET, queryset=user_list)
    return render(request, 'index.html', {'filter': blog_filter})


class NewBlogView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "create_blog.html"
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = "profile.html"
    context_object_name = 'blog_entries'
    paginate_by = 3

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user).order_by('-date')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blog = self.get_object()
        return blog.author == self.request.user


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    success_url = '/'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blog = self.get_object()
        return blog.author == self.request.user
