# coding: utf-8
# author: dlyapun

# from django.shortcuts import render_to_response
# from django.template import RequestContext
from django.views.generic import ListView, DetailView
from force_blog.models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    context_object_name = 'blog_posts'

    paginate_by = 5


class BlogPostDetailView(DetailView):
    model = BlogPost
