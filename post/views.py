from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timesince, timezone
from user.models import User

from .forms import CommentForm, PostForm, ProfileForm
from .models import Comment, Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.nickname
            post.published_date = timezone.now()
            post.save()
            return redirect('post:post_detail', pk=post.pk)
    else: 
        form = PostForm()
        return render(request, 'post/post_new.html', {'form':form})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(Post_id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.Post = post
            comment.user = request.user
            comment.save()
            form = CommentForm()
            return render(request, 'post/post_detail.html', {'post': post, 'form':form, 'comments':comments})
        else:
            return redirect('post:post_list')
    else:
        form = CommentForm()
        return render(request, 'post/post_detail.html', {'post': post, 'form':form, 'comments':comments})

def post_edit(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user.nickname
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else: 
        form = PostForm(instance = post)
    return render(request, 'post/post_new.html', {'form':form})


def likes(request, pk):
    like_p = get_object_or_404(Post, pk=pk)
    if request.user in like_p.like.all():
        like_p.like.remove(request.user)
        like_p.like_count -= 1
        like_p.save()
    else:
        like_p.like.add(request.user)
        like_p.like_count += 1
        like_p.save()
    return redirect('post:post_list')

def comment_delete(request, pk, a):
    comment = get_object_or_404(Comment, pk=pk)
    Comment.objects.filter(user = request.user, pk = comment.pk).delete()
    post = get_object_or_404(Post, pk = a)
    return redirect('post:post_detail', pk=post.pk)
    

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.nickname == post.author:
        post.delete()
    return redirect('post:post_list')

def profile(request,pk):
    profile = get_object_or_404(User, pk=pk)
    return render(request, 'post/my_page.html', {'profile':profile})




def profile_edit(request,pk):
    profile = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form= ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.prof_img = request.POST.img
            profile.save()
            return redirect('post:my_page', pk=profile.pk)
        else:
            return render(request, 'post/profile_edit.html', {'form':form})
    form = ProfileForm(instance=profile)
    return render(request, 'post/profile_edit.html', {'form':form})
        




# Create your views here.
