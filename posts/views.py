from django.shortcuts import render
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm

def posts(request):
    posts = Post.objects.all()
    field_names = [f.name.capitalize() for f in Post._meta.get_fields()]
    field_names = list(filter(lambda f: f != 'Id', field_names))

    return render(request, 'posts/posts.html', {'posts': posts, 'fields': field_names})

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts')
    else:
        form = PostForm()
    return render(request, 'posts/add_post.html', {'form': form})
