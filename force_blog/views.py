# coding: utf-8
# author: dlyapun

# from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from profile.models import CustomUser
from django.http import Http404
from django.shortcuts import render_to_response, redirect
from django.views.generic import ListView, DetailView
from force_blog.forms import BlogPostForm
from force_blog.models import BlogPost
from django.template import RequestContext


class BlogPostListView(ListView):
    model = BlogPost
    context_object_name = 'blog_posts'

    paginate_by = 5

    def get_queryset(self):
        qs = BlogPost.objects.filter(state=1)
        return qs


class BlogPostDetailView(DetailView):
    model = BlogPost

    context_object_name = 'blogpost'


@login_required
def blog_edit(request, id):
    owner = CustomUser.objects.get(user=request.user)
    blog = BlogPost.objects.get(id=int(id))

    if blog.owner.user != request.user:
        return Http404

    if request.POST:
        form = BlogPostForm(request.POST, instance=blog)
        if form.is_valid():
            form.save(owner=owner)
            return redirect('/')
    else:
        form = BlogPostForm(instance=blog)

    data = {'form': form, 'blogpost': blog}
    return render_to_response('force_blog/blogpost_edit.html',
                              data,
                              context_instance=RequestContext(request))


@login_required
def hidden_blog(request):
    if request.POST:
        blog_id = request.POST['blog_id']
        blog = BlogPost.objects.get(id=int(blog_id))
        blog.state = BlogPost.DISABLE
        blog.save()
        return redirect('/blog/')
    else:
        return redirect(blog.get_absolute_url())
