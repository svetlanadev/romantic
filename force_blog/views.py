# coding: utf-8
# author: dlyapun

# from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from profile.models import CustomUser
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, render
from django.views.generic import ListView, DetailView
from force_blog.forms import BlogPostForm
from force_blog.models import BlogPost, BlogEdit, Category
from django.template import RequestContext


class BlogPostListView(ListView):
    model = BlogPost
    context_object_name = 'blog_posts'

    paginate_by = 5

    def get_queryset(self):
        qs = BlogPost.objects.select_related('owner', 'owner__user').prefetch_related('category', 'karma_users').filter(state=1)
        return qs


    def get_context_data(self, **kwargs):
        context = super(BlogPostListView, self).get_context_data(**kwargs)
        return context


class BlogPostListViewTag(BlogPostListView):

    def get_queryset(self, **kwargs):
        category = self.kwargs['category_id']
        return super(BlogPostListViewTag, self).get_queryset().filter(category=category)


class BlogPostDetailView(DetailView):
    model = BlogPost

    context_object_name = 'blogpost'


@login_required
def blog_edit(request):
    user = CustomUser.objects.get(user=request.user)
    id_blog = request.POST['id_blog']
    blog = BlogPost.objects.get(id=id_blog)

    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=blog)
        if form.is_valid():
            blog_save = blog
            blog_save.title = blog_save.title + 'backup'
            blog_edit = BlogEdit(user_edit=user)
            blog_edit.save()
            blog_save.blog_edit.add(blog_edit)
            blog_save.state = 0
            blog_save.pk = None
            blog_save.save()
            print "ALL OK"
            form.save()
            url = u'/blog/%s' % id_blog
            return redirect(url)

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


@login_required
def karma_force_blog(request):
    user = CustomUser.objects.get(user=request.user)
    if request.method == "POST":
        if user.karma < -10:
            message = "Недостаточно кармы для голосования"
            print message
            pass
        id_blogpost = request.POST['id_blogpost']
        karma = request.POST['karma']
        blogpost = BlogPost.objects.get(id=id_blogpost)
        if user in blogpost.karma_users.all():
            message = "Вы уже поставили рейтинг"
            print message
        else:
            if karma == "minus":
                blogpost.rating = blogpost.rating - 1
                user.karma = user.karma - 3
            if karma == "plus":
                blogpost.rating = blogpost.rating + 1
                user.karma = user.karma + 3
            blogpost.save()
            user.save()
            blogpost.karma_users.add(user)
    else: 
        return redirect('/')            
    return redirect(blogpost.get_absolute_url())


def search_for_tag(request, category_id):
    category = Category.objects.get(id=category_id)
    blog_posts = BlogPost.objects.select_related('owner', 'owner__user').prefetch_related('category', 'karma_users').filter(category=category)
    data = {'blog_posts': blog_posts, 'paginate_by': 5}
    return render_to_response('force_blog/blogpost_list.html',
                              data,
                              context_instance=RequestContext(request))   