from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

def forum(request):
    posts = Post.objects.all().order_by('-created')
    return render(request, "Forum/forum.html", {"posts": posts})

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('forum')
    else:
        form = PostForm()
    return render(request, "Forum/new_post.html", {"form": form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if (post.author == request.user or request.user.is_superuser) and request.method == "POST":
        post.delete()
    return redirect('forum')

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id = post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('forum',)
    else:
        form = PostForm(instance=post)

    return render(request, 'Forum/edit_post.html', {'form': form})