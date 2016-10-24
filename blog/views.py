from django.core import paginator
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, cookie
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template.context_processors import csrf
from django.utils import timezone
from .models import Post, Comments
from .forms import PostForm, CommentsForm
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def post_list(request, page_number=1):
    posts1 = Post.objects.all()
    paginator = Paginator(posts1,3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    username = auth.get_user(request).username
    return render(request, 'blog/post_list.html', {'posts': posts, 'username': username})


def post_detail(request, pk):
    comments_form = CommentsForm
    args = {}
    args.update(csrf(request))
    args['post'] = Post.objects.get(pk=pk)
    args['comments'] = Comments.objects.filter(comments_article_id=pk)
    args['form'] = comments_form
    args['username'] = auth.get_user(request).username
    return render(request,'blog/post_detail.html', args )


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)

    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def addlike(request, pk):
    try:
        if pk in request.COOKIES:
            return_path = request.META.get('HTTP_REFERER','/')
            return redirect(return_path)
        else:
            post = Post.objects.get(id=pk)
            post.likes +=1
            post.save()
            return_path = request.META.get('HTTP_REFERER', '/')
            response = redirect(return_path)
            response.set_cookie(pk, "test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')

def addcomment(request, pk):
    if request.POST:
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article_id = Post.objects.get(id=pk)
            comment.comments_author = request.user
            form.save()
    return redirect('/post/%s/' % pk)

def adddislike(request, pk):
    try:
        if pk in request.COOKIES:
            return_path = request.META.get('HTTP_REFERER','/')
            return redirect(return_path)
        else:
            post = Post.objects.get(id=pk)
            post.dislikes +=1
            post.save()
            return_path = request.META.get('HTTP_REFERER', '/')
            response = redirect(return_path)
            response.set_cookie(pk, "test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')